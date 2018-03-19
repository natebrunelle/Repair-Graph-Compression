# Repair Compression for Graphs

 [![Master](https://travis-ci.com/yonathanF/Repair-Graph-Compression.svg?token=iEJ27eCnjKeFqxrBkzzA&branch=master)](https://travis-ci.com/yonathanF/Repair-Graph-Compression)
 [![Dev](https://travis-ci.com/yonathanF/Repair-Graph-Compression.svg?token=iEJ27eCnjKeFqxrBkzzA&branch=development)](https://travis-ci.com/yonathanF/Repair-Graph-Compression)

### Setup

1. Make sure you have pip (check version, current version is 9.0) 
```python 
pip -V 
```

2. Install all packages
```python 
pip install -r requirements.txt
```

### Documentation 
- Follow the PEP 8 standard when documenting your code 
- Look for a python linting plugin/lib for your IDE/system 
- Leave commit messages with helpful messages. Try to do a single subject line, followed by more descripiton
- Push to the right branch. Master is already locked so you need to do a pull request before merging into master
	- Try to stick to the Git Workflow [Details here](https://www.atlassian.com/git/tutorials/comparing-workflows)


### Testing 
- Write good unit test cases, and cover at least the happy path
- We have [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.5.1/) for line coverage (shoot for 80% or so). The master branch will probably start rejecting anything below 80% 
- Use the standard python Unittest 
- Travis CI is connected and active. It will run our complete test suite so if you don't feel like running all tests, test the code you changed/added, then push. Travis CI will run all the tests on the CI server and send emails if tests fail.
- Write your unit tests inside /Test. Make sure your files start with 'test' (you can override this is but lets not) 
-  
### File Organization 
- Graph directory --> contains all files for the graph, node, cluster, etc 
- Repair directory --> compression, decompression, etc 
- Algorithms --> the algos we have written so far (search, sort, etc) 
- Utils --> extra stuff like the graph visualizer 
- Tests --> holds all the tests [we will break this into two when we have integration tests]

### Helpful commands 
- Running tests 
```python
python -m unittest tests.test_XXX 
```
- Running coverage (see coverage of the repair folder for example)
```python 
coverage run --source=repair/ -m unittest discover -s Tests/
```

- Then use this to generate the html and view the report in your browser 
```python
coverage html
```
- To get style suggestions etc (if your IDE doesn't have a plugin)
```python 
pep8 python_file.py
```

- To update all your branches 
```bash 
git pull --all 
```

- To see your branches 
```bash
git branch
```


