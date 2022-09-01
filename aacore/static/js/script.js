//REQUETES AJAX
$(document).ready(function() {

        // OUVERTURE DES PAGES PAR CLIC SUR PHOTO
        $("#exposant").click(function(e) {
                window.open("/exposant/exposants", '_parent');
        })

        $("#visiteur").click(function(e) {
                window.open("/infosfoire/horaires_tarifs", '_parent');
        })

        $("#theme").click(function(e) {
                window.open("/animation/animations_cheval", '_parent');
        })

        $("#dossier_gastronomie").click(function(e) {
                window.open("/exposant/dossier_gastronomie", '_parent');
        })

        $("#dossier_autres").click(function(e) {
                window.open("/exposant/dossier_autres", '_parent');
        })

        $("#air_libre").click(function(e) {
                window.open("/exposant/air_libre", '_parent');
        })

        $("#camion_exposition").click(function(e) {
                window.open("/exposant/camion_exposition", '_parent');
        })

        $("#stand").click(function(e) {
                window.open("/exposant/stand", '_parent');
        })

        $("#module_3x3").click(function(e) {
                window.open("/exposant/module_3x3", '_parent');
        })

        $("#chapiteau").click(function(e) {
                window.open("/exposant/chapiteau", '_parent');
        })

        $("#menu1").click(function() {
                sousMenuOff();
                //$("#nav_tel").addClass('menu_off');
        })

        $("#menu_burger").click(function(){
                if ($("#nav_tel").hasClass('menu_off'))
                     $("#nav_tel").removeClass('menu_off');
                else
                     $("#nav_tel").addClass('menu_off');
        })


})


function ancre() {
        location.href = "#jumelage";
}


function sousmenu(id) {
        sousMenuOff(id);
        document.getElementById("sous-menu" + id).style.display = "flex";
}


function sousMenuOff() {
        nb = 4;
        for (let pas = 1; pas <= nb; pas++) {
                document.getElementById("sous-menu" + pas).style.display = "none";
        }
}