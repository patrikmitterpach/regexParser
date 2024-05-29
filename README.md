<a name="readme-top"></a>

<div align="center">
  
  [![LinkedIn][linkedin-shield]][linkedin-url]
  [![GPL License][license-shield]][license-url]
  ![Size](https://img.shields.io/github/languages/code-size/patrikmitterpach/regexParser?color=green&style=for-the-badge)
  ![Last Commit](https://img.shields.io/github/last-commit/patrikmitterpach/regexParser?color=green&style=for-the-badge)

  </div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/patrikmitterpach/regexParser">
    <img src="https://user-images.githubusercontent.com/5418178/175823761-ee7996b9-57be-4abf-be93-0ad25e7f37f0.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">regexParser.py</h3>

  <p align="center">
    A recursion based regex parser and matcher, complete with a CI/CD testing pipeline.
    <br />
    <br />
    ·
    <a href="https://github.com/patrikmitterpach/regexParser#installation">Installation</a>
    ·
    <a href="https://github.com/patrikmitterpach/regexParser/blob/main/LICENSE.txt">License</a>
  </p>
</div>

## About
This code is aimed at matching basic regex queries. This is done in two steps: parsing and matching. The regex pattern is first decoded into a tree structure, then the target text is matched against the desired tree structure.


## Installation

To install, clone the repository by running the following command:

```cmd
git clone https://github.com/patrikmitterpach/regexParser
```

Afterwards, open the folder in your terminal and install the required dependencies and the code itself as a local package:

1. `cd regexParser`
2. `pip install -r requirements`
3. `pip install -e .`

Finally, launch the test with the pytest testing suite:

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

