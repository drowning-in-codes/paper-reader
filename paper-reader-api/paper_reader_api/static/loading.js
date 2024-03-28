'use strict'
function loading(){
    let loader = document.getElementById('loading');
    console.log(loader)
    loader.style.display = 'inline-block';
    loader.style.visibility = 'visible';
    loader.style.opacity = 1;

    let detail_paper = document.getElementById('detail_paper');
    detail_paper.style.display = 'none';
    detail_paper.style.opacity = 0;
}
