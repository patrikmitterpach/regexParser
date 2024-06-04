<a name="readme-top"></a>

<div align="center">
  
  ![Build Status](https://img.shields.io/github/check-runs/patrikmitterpach/regexparser/master?color=green&style=for-the-badge)
  ![Last Commit](https://img.shields.io/github/last-commit/patrikmitterpach/regexParser?color=green&style=for-the-badge)
  ![Size](https://img.shields.io/github/languages/code-size/patrikmitterpach/regexParser?color=green&style=for-the-badge)
  [![GPL License][license-shield]][license-url]
  [![LinkedIn][linkedin-shield]][linkedin-url]

  </div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/patrikmitterpach/regexParser">
    <img src="https://user-images.githubusercontent.com/5418178/175823761-ee7996b9-57be-4abf-be93-0ad25e7f37f0.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">regexParser.py</h3>

  <p align="center">
    A recursion based regex parser and matcher
    <br />
    <a href="https://github.com/patrikmitterpach/regexParser#installation">Installation</a>
    ·
    <a href="https://github.com/patrikmitterpach/regexParser/blob/main/LICENSE.txt">License</a>
  </p>
</div>

## About
The aim of this project is to create a basic, recursion-based regular expression parser and matcher, bundled with a usable program that replicates the basic functions of a program such as `sed` or `grep`. Furthermore, all the functionalities are to be tested automatically with a continuous integration pipeline. 


## Installation

To install, clone the repository by running the following command:

```cmd
git clone https://github.com/patrikmitterpach/regexParser
```

Afterwards, open the folder in your terminal and install the required dependencies and the code as a local package:

1. `cd regexParser`
2. `pip install -r requirements`
3. `pip install -e .`

## Usage


Launch the app with `python3 source/regexParser/main.py`. By providing additional parameters, you can specify the desired regex query as well as the location of the text file on which the query should be run. By default, the query `".* "` is run upon the file provided within the repository, the first chapter of Seneca's *On the Shortness of Life*.

![image](https://github.com/patrikmitterpach/regexParser/assets/59344031/430b0b03-821d-473c-8067-a03ba171a5f6)



4. `pytest`

<!-- LICENSE -->
## License

Distributed under the GPL3 License. See `LICENSE.txt` for [more information](https://github.com/patrikmitterpach/F1DB/blob/master/LICENSE.txt).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[license-shield]: https://img.shields.io/badge/LICENSE-GPL3-green?style=for-the-badge
[license-url]: https://github.com/patrikmitterpach/regexParser/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/patrikmitterpach

