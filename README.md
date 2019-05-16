##### TASK:
I need to develop a web application using Python that reads a collection of JSON files (up to 500) that are stored in a local directory. The expected output will be:


  - Simple charts from data that is read from the JSON files (bar charts, pie charts, etc.)
  - Produce Powerpoint and excel files from JSON data (tables mostly)
  - Develop a front end HTML page where the charts are displayed based on simple user selection using any bootstrapping front-end framework
  - Package everything in a docker container to be ported to a different web server

There is no database here. All the data is stored in JSON files and they will be updated on timely bases which are to be parsed.

##### REQUIREMENTS:

  - The code MUST be commented extensively

  - The job will be in 4 phases as described above
  
  
###### USEFUL COMMANDS

docker build -t json-plot:latest .
docker run -d -v $(pwd):/app -p 8000:8000 json-plot
  