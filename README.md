# QA Test Project
Project for simulating QA tests setup and maintenance.

## Development Notes
### Requirements
* Maven 3.6.3
* Python 3.10.12

### First Time Setup
```
python3 -m pip install -r requirements.txt
playwright install-dep
playwright install
```

### Test Execution
* Execute all tests: `mvn test`
  * Add `-Dinclude={feature_filename_pattern}` to specify feature files to include.
  * Add `-Dexclude={feature_filename_pattern}` to specify feature files to exclude.

### Contribution
#### Adding a Feature
* Create a new file in `features` directory.
  * Use `.feature` extension.
  * Use `snake_case` for file names to avoid filesystem complications.
* Reference [Gherkin](https://cucumber.io/docs/gherkin/reference) for BDD syntax.
