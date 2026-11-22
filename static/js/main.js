
const navLinks=document.querySelectorAll(".nav-link");
const views=document.querySelectorAll(".view");
const gameFrame=document.getElementById("game-frame");

navLinks.forEach(link=>{
    link.addEventListener("click",function(e){
        e.preventDefault();
        views.forEach(v=>v.classList.add("hidden"));
        const targetId=this.getAttribute("data-target");
        const targetView=document.getElementById(targetId);
        if (targetView){
            targetView.classList.remove("hidden");
        }
        if (targetId==="view-game" && !gameFrame.getAttribute("src")){
            gameFrame.src=gameFrame.getAttribute("data-src")
        }
        if (targetId!=="view-game" && gameFrame.getAttribute("src")){
            gameFrame.src="";
        }
    });
});


