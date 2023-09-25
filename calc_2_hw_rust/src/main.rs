use std::{fs, env};
use chrono::{DateTime, Local};
use serde::{Serialize, Deserialize};
mod content_parser;

#[derive(Serialize, Deserialize, Debug, Clone)]
struct CourseData {
    assignments: Vec<Assignment>
}

#[derive(Serialize, Deserialize, Debug, Clone)]
struct Assignment {
    title: String,
    content: String,
    #[serde(rename = "dueAt")]
    due_at: Option<DateTime<Local>>,
}

fn find_nearest_due_date(due_dates: Vec<DateTime<Local>>, target: DateTime<Local>) -> usize {
    let mut l = 0;
    let mut r = due_dates.len() - 1;

    if target <= due_dates[0] {
        return 0
    }

    else if target > due_dates[r] {
        return 0
    }

    while l <= r {
        let m = (l + r) / 2;

        if due_dates[m - 1] <= target && target <= due_dates[m] {
            return m.try_into().unwrap();
        }

        else if target > due_dates[m] {
            l = m + 1;
        }

        else if target < due_dates[m-1] {
            r = m - 1;
        }
    }
    0
}

fn main() {
    env::set_current_dir(env::current_exe().unwrap().parent().unwrap()).expect("Weird path");
    const COURSE_DATA_PATH: &str = "./course-data.js";
    let file_contents = match fs::read_to_string(COURSE_DATA_PATH) {
        Ok(contents) => contents,
        Err(err) => {
            println!("Current Path: {:?}", std::env::current_dir().unwrap());
            panic!("Can't find course-data.js");
        }
    };
    let course_data: CourseData = serde_json::from_str(&file_contents).expect("Failed to parse JSON");
    let assignments = course_data.assignments;
    let mut hw_assignments: Vec<Assignment> = assignments
        .into_iter()
        .filter(|a| a.title.starts_with("Homework") && a.due_at.is_some())
        .collect();

    hw_assignments.sort_by_key(|a| a.due_at);
    let current_date: DateTime<Local> = Local::now();
    let due_dates: &Vec<DateTime<Local>> = &hw_assignments
        .iter()
        .map(|a| a.due_at.unwrap())
        .collect();

    let assignment_index: usize = find_nearest_due_date(due_dates.clone(), current_date);
    let cur_assignment = &hw_assignments[assignment_index];
    let cur_content: &str  = &cur_assignment.content;
    let problems = content_parser::parse_content(cur_content);
    println!("{}", &cur_assignment.title);
    println!("Due {:?}", &cur_assignment.due_at.unwrap().date_naive());
    println!("{}", problems);
}
