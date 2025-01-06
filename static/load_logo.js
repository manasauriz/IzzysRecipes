document.addEventListener('DOMContentLoaded', function() {
    const container = document.createElement('div');

    const link = document.createElement('a');
    link.href = '/';

    const logo = document.createElement('img');
    logo.src = "static/logo.png";
    logo.alt = "Home";
    logo.width = 100;
    logo.height = 75;

    link.appendChild(logo);
    container.appendChild(link);

    document.body.insertAdjacentElement('afterbegin', document.createElement('hr'));
    document.body.insertAdjacentElement('afterbegin', container);
});
