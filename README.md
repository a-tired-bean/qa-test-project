# QA Test Project
Project for simulating QA tests setup and maintenance.

## Development Notes
### Requirements
* Python 3.10.12

### First Time Setup
`python3 -m pip install -r requirements.txt`

### Test Execution
* Execute all tests: `behave`
* Execute specific tests: `behave -i {feature_filename_pattern}`
* Execute all excluding specific tests: `behave -e {feature_filename_pattern}`

### Contribution
#### Adding a Feature
* Create a new file in `features` directory.
  * Use `.feature` extension.
  * Use `snake_case` for file names to avoid filesystem complications.
* Reference [Gherkin](https://cucumber.io/docs/gherkin/reference) for BDD syntax.
