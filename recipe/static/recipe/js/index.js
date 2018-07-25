var clickIcons = document.getElementById('click-icons');
var clickNav = document.getElementById('click-nav');
var clickFilter = document.getElementById('click-filter');
var closeNav = document.getElementById('close-nav');
var closeFilter = document.getElementById('close-filter');
var nav = document.getElementsByTagName('nav')[0];
var recipeFilter = document.getElementById('recipe-filter');

if(window.outerWidth <= 1023){
    nav.style.display = 'none';
};

if (recipeFilter){
    recipeFilter.style.display = 'none';
} else {
    document.getElementById('click-filter').style.display = 'none';
};

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

if (recipeFilter){
    closeFilter.onclick = function(){
        recipeFilter.style.display = 'none';
        clickIcons.style.display = 'flex';
    }
};
