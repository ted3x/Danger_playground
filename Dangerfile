# Sometimes it's a README fix, or something like that - which isn't relevant for
# including in a project's CHANGELOG for example
# declared_trivial = github.pr_title.include? "#trivial"

# Make it more obvious that a PR is a work in progress and shouldn't be merged yet
warn("PR is classed as Work in Progress") if github.pr_title.include? "[WIP]"

# Warn when there is a big PR
# warn("Big PR") if git.lines_of_code > 500

# ktlint
checkstyle_format.base_path = Dir.pwd
checkstyle_format.report '/bitrise/src/build/reports/ktlint/ktlint-report.xml'

# AndroidLint
android_lint.report_file = "/bitrise/src/build/reports/lint/lint-report.xml"
android_lint.skip_gradle_task = true
android_lint.severity = "Warning"
android_lint.lint(inline_mode: true)