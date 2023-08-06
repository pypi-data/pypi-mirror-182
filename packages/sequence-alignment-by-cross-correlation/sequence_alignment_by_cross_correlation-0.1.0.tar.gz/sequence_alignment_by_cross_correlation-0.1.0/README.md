<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kuhjuice/sequence_alignment_by_cross_correlation">
    <img style='border-radius:30px' src="images/logo.png" alt="Logo" width="120" height="120">
  </a>

<h3 align="center">Sequence Alignment<br>by cross correlation</h3>

  <p align="center">
    This is an implementation of the cross correlation algorithm for DNA/RNA alignment
    <br />
    <a href="https://github.com/kuhjuice/sequence_alignment_by_cross_correlation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/kuhjuice/sequence_alignment_by_cross_correlation">View Demo</a>
    ·
    -->
    <a href="https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/issues">Report Bug</a>
    ·
    <a href="https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The project is based on the paper [Sequence Alignment by Cross-Correlation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2291754/) and bridges the gap between the knowledge and an useful implementation. The underlying technique is the cross correlation algorithm, which can be tested in this [notebook](https://makeabilitylab.github.io/physcomp/signals/ComparingSignals/index.html).

Another [notebook](https://colab.research.google.com/drive/1XC0AIqli6igxuDt0phcmZCu5IK5tiV7W?usp=sharing) can be seen here. The focus of this notebook is to illustrate how we can use the cross correlation for genomic data.

The gene sequences were obtained using the [NCBI](https://www.ncbi.nlm.nih.gov/gene/) database.

![Example Screen Shot][product-screenshot]

<!-- Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `kuhjuice`, `sequence_alignment_by_cross_correlation`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description` -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python3: https://realpython.com/installing-python/

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kuhjuice/sequence_alignment_by_cross_correlation.git
   ```
2. Navigate into the repo
   ```sh
   cd sequence_alignment_by_cross_correlation
   ```
3. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
   or
   ```sh
   pip3 install -r requirements.txt
   ```
4. Ask the CLI for help with
   ```sh
   python3 sequence_alignment_by_cross_correlation.py --help
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### Example 1
If we want to get an understanding of what the tool can do for us, we can use the help function of the CLI.
```sh
python3 sequence_alignment_by_cross_correlation/sequence_alignment_by_cross_correlation.py --help
```
![Help Screen Shot][help-screenshot]
### Example 2
If we want to find the gene omcB in the genome of Chlamydia Trachomatis we can use the sequence files in `sequencesToTest`

Executing the following will search for the omcB Gene in the genome of Chlamydia Trachomatis

   ```sh
python3 sequence_alignment_by_cross_correlation/sequence_alignment_by_cross_correlation.py 'sequencesToTest/C_T_genome.fasta' 'sequencesToTest/omcB_C_T_100fit.fna'
   ```

![Usage Screen Shot][usage-screenshot]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Fix Bugs
- [ ] Make it a real package
- [ ] Evalueate if useful for other projects

See the [open issues](https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bo Kern - [@blood_in_the_water@chaos.social ](https://chaos.social/@blood_in_the_water) - bo@blackscript.de

Project Link: [https://github.com/kuhjuice/sequence_alignment_by_cross_correlation](https://github.com/kuhjuice/sequence_alignment_by_cross_correlation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [TU-Berlin](tu.berlin)
* [Carmen Regner](https://www.tu.berlin/mikrobiologie/ueber-uns/team-personen/#c422452)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kuhjuice/sequence_alignment_by_cross_correlation.svg?style=for-the-badge
[contributors-url]: https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kuhjuice/sequence_alignment_by_cross_correlation.svg?style=for-the-badge
[forks-url]: https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/network/members
[stars-shield]: https://img.shields.io/github/stars/kuhjuice/sequence_alignment_by_cross_correlation.svg?style=for-the-badge
[stars-url]: https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/stargazers
[issues-shield]: https://img.shields.io/github/issues/kuhjuice/sequence_alignment_by_cross_correlation.svg?style=for-the-badge
[issues-url]: https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/issues
[license-shield]: https://img.shields.io/github/license/kuhjuice/sequence_alignment_by_cross_correlation.svg?style=for-the-badge
[license-url]: https://github.com/kuhjuice/sequence_alignment_by_cross_correlation/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/bpbk
[product-screenshot]: images/productScreenshot.png
[usage-screenshot]: images/usagescreenshot.png
[help-screenshot]: images/helpScreenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
