# This repository is a Demo for [**GenBenchSite**](https://github.com/White-On/BenchSite), a Benchmarking tools for libraries.

## Files organisation

- `project.ini`: Contains the configuration for the project. It is used to configure the website and the benchmarking process.
- `res/`: Contains the resources for the website, such as logos, images, etc. The script will copy the content of this folder to the `pages/assets/` folder.
- `targets/`: Contains the targets to be benchmarked. Each target is a folder containing a `target.ini` file containing the configuration for the target and a `description.html` to describe the target (the file be be added to the page of the target).
- `themes/`: Contains the themes for the task. Each theme is a folder containing a `theme.ini` file containing the configuration for the theme and a `description.html` to describe the theme (the file be be added to the page of the theme).In each theme folder:
    - `task/`: Contains the tasks for the theme. Each task is a folder containing a `task.ini` file containing the configuration for the task and a `description.html` to describe the task (the file be be added to the page of the task).There's also a `extra.html` file that will be added to the page of the task. the `data/` folder is where you can put the data used by your test scripts .Each task folder also contains folders for each target to be benchmarked. Each target folder contains the test scripts for the target. ( a `run` script and a `before` script if needed ). The `evaluation` script is used to evaluate the results of the benchmarking process found in the `output/` folder.


====================
- `pages/`: Contrains the pages of the website generated by the benchmarking process.

## How to use

1. Get the [**GenBenchSite**](https://github.com/White-On/BenchSite) package either by downloading with the command
```pip install genbenchsite``` it or by cloning it. Then you'll have access to the `gbs` command with the help of the command ```gbs help```.
1. Create a template folder for your project with the command ```gbs init <nameBenchmark>```
1. Edit the files to configure your project.
1. Run the benchmarking process with the command ```gbs benchmark -I <pathToTemplateFolder>``` ( the default path is the current directory ). The process will generate the data in the `results.json` folder.
1. Run the website generation process with the command ```gbs website -I <pathToTemplateFolder>``` ( the default path is the current directory ). The process will generate the website in the `pages/` folder.

## Website UI

You'll find the website in the pages folder and is composed of `index.html`, the main pages `content/`, with all the pages generated by the benchmarking process,`script/` for  all the *javascript* files, `style/` with all the *css* files, and `assets/` with all the assets needed for the website.

the main page is `index.html` and should look like this:

You can navigate through the pages using the navigation bar on the left side of the page. The **data** created by the benchmarking process can be downloaded using the **Raw Data** button on the top right of the page.