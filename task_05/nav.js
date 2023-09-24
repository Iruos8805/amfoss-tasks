class Header extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <nav>
        <h1>
          <a href="web.html"> <!-- Link to web.html -->
            <img src="https://github.com/amfoss/tasks/blob/2023/task-05/assets/navbar/logo.png?raw=true" alt="Logo">
          </a>
        </h1>
        <ul>
          <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q">
            <img src="https://github.com/amfoss/tasks/blob/2023/task-05/assets/navbar/spotify.png?raw=true" alt="Spotify">
          </a></li>
          <li><a href="https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA">
            <img src="https://w1.pngwing.com/pngs/984/730/png-transparent-youtube-play-logo-youtube-play-buttons-video-facebook-blue-aqua-green-teal-thumbnail.png" alt="YouTube">
          </a></li>
          <li><a href="https://twitter.com/Imaginedragons">
            <img src="https://raw.githubusercontent.com/amfoss/tasks/e87c95ffff74c77eb09a0258e26b56e7d17a281e/task-05/assets/navbar/twitter.svg" alt="Twitter">
          </a></li>
        </ul>
      </nav>
    `;
  }
}

customElements.define('custom-header', Header);
