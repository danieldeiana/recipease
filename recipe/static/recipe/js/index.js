var clickIcons = document.getElementById('click-icons');
var clickNav = document.getElementById('click-nav');
var clickFilter = document.getElementById('click-filter');
var closeNav = document.getElementById('close-nav');
var closeFilter = document.getElementById('close-filter');
var nav = document.getElementsByTagName('nav')[0];
var recipeFilter = document.getElementById('recipe-filter');

nav.style.display = 'none';
recipeFilter.style.display = 'none';

clickNav.onclick = function(){
    nav.style.display = 'flex';
    clickIcons.style.display = 'none';
};

clickFilter.onclick = function(){
    recipeFilter.style.display = 'block';
    clickIcons.style.display = 'none';
};

closeNav.onclick = function(){
    nav.style.display = 'none';
    clickIcons.style.display = 'flex';
}

closeFilter.onclick = function(){
    recipeFilter.style.display = 'none';
    clickIcons.style.display = 'flex';
}
