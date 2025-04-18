//for all pages (Hamburger menu)
function HamburgerMenu(){
    const hamMenu = document.querySelector(".ham-menu");

    const sideBar = document.querySelector(".sidebar");
    hamMenu.classList.toggle("active");
    sideBar.classList.toggle("active");

}
// for contact page
function goToLinkedIn(){
    window.open("https://www.linkedin.com/in/wyatt-evans-66b8a62b7/", '_blank');
}

function goToGitHub(){
    window.open("https://github.com/wevans02", '_blank');
}

