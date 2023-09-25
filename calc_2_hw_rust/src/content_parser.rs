pub fn parse_content(content: &str) -> &str {
    let content = content.lines().nth(1).unwrap().trim_end_matches("</p>").trim_start_matches("<p>");
    content
}
