<div id="readme-top" align="center">

[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![Stargazers][stars-shield]][stars-url]
[![AGLP License][license-shield]][license-url]

</div>

<div>
<h1 align="center">ESP32 Fox Zero</h1>

  <p align="center">
    Open source Flipper like device made with Micropython, an ESP32 and some modules.
    <br />
  </p>
</div>

> [!WARNING]
> This project was made for educational purposes, it is intended for legal and authorized security testing only. Use of this software for any malicious or unauthorized activities is strictly prohibited. The developers assume no liability for any misuse of the software. Use at your own risk.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#hardware">Hardware</a></li>
    <li><a href="#installation/flashing">Installation/Flashing</a></li>
    <li>
      <a href="#features">Features</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact-and-funding">Contact and Funding</a></li>
  </ol>
</details>


## About The Project

The ESP32 Fox Zero project is a flexible, budget-friendly option for those interested in learning about hardware and software integration. Built around the ESP32 microcontroller and using Micropython, it's a great tool for hobbyists, students, and developers to explore wireless communication, sensor interaction, and more.

As an open-source project, it encourages community involvement, with a repository that includes detailed guides, schematics, and code examples. Micropython makes it beginner-friendly, so even those new to coding can easily understand and modify the project.

The hardware setup features an ESP32, a display, NFC/RFID and sub-GHz modules, an infrared transmitter/receiver, and buttons. Its modular design allows for customization, and step-by-step instructions make assembly straightforward.

This project is a practical way to dive into embedded systems and IoT, offering plenty of opportunities to learn and innovate. Whether you're just starting out or have experience, it's a great way to experiment, build, and contribute to an active open-source community.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[![Micropython][micropython]][micro-url]

[![ESP-IDF][esp]][esp-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Hardware

For this project you can use the hardware that better suits you, but the tested one currently consists:

- ESP32 C3 Mini 1 N4 Risc-V
- LCD TFT Display
- MicroSD Card Module
- 433MHz RF Transmiter and Receiver
- NFC/RFID Reader
- IR Encoder Decoder Tx Rx lo

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Installation/Flashing

```To be implemented```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Features

### WiFi

- [ ] Connect to WiFi
- [ ] WiFi AP
- [X] Scanner
- [X] Packet Sniffer
- [ ] TCP Client
- [ ] TCP Listener
- [X] WiFi Attacks
  - [X] Bruteforce
  - [ ] Beacon Spam
- [ ] Captive Portal

### Bluetooth

- [ ] Scanner
- [ ] Jammer
- [ ] Bad BLE

### RFID

- [ ] Read Tag
- [ ] Clone Tag
- [ ] Write Data
- [ ] Erase Data
- [ ] Save File
- [ ] Load File
- [ ] Emulate Tag

### Radio

- [ ] FM Spectrum
- [ ] Broadcast Standart
- [ ] Broadcast Stop

### IR

- [ ] TV Controller
- [ ] IR Receiver 

### Others

- [X] Micropython REPL
- [ ] SD Card Manager

See the [open issues](https://github.com/alicepfp/esp32-fox-zero/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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



## License

Distributed under the AGPL-3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact and Funding

[![LinkedIn][linkedin-shield]][linkedin-url]

[![Github][git]][git-url]

[![BuyMeACoffee][coffee]][coffee-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[forks-shield]: https://img.shields.io/github/forks/alicepfp/esp32-flipper.svg?style=for-the-badge
[forks-url]: https://github.com/alicepfp/esp32-fox-zero/network/members
[stars-shield]: https://img.shields.io/github/stars/alicepfp/esp32-flipper.svg?style=for-the-badge&color=yellow
[stars-url]: https://github.com/alicepfp/esp32-fox-zero/stargazers
[issues-shield]: https://img.shields.io/github/issues/alicepfp/esp32-flipper.svg?style=for-the-badge
[issues-url]: https://github.com/alicepfp/esp32-fox-zero/issues
[license-shield]: https://img.shields.io/github/license/alicepfp/esp32-flipper.svg?style=for-the-badge
[license-url]: https://github.com/alicepfp/esp32-fox-zero/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/linkedin_username
[python]: https://img.shields.io/badge/python-gray?style=for-the-badge&logo=python&logoColor=white&labelColor=blue
[git]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[git-url]: https://github.com/alicepfp
[micropython]: https://img.shields.io/badge/Micropython-black?style=for-the-badge&logo=micropython&logoColor=white
[micro-url]: https://micropython.org/
[esp]: https://img.shields.io/badge/espressif-E7352C?style=for-the-badge&logo=espressif&logoColor=white
[esp-url]: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/index.html
[coffee]: https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black
[coffee-url]: https://buymeacoffee.com/alicepfp