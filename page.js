  window.addEventListener('scroll', function() {            /*realisée a l'aide de chatgpt*/
    var bandeau = document.querySelector('.bandeau');
    var limite = 80;
    var menu = document.querySelector('.menu');
    var menu_actif = true;

  
    if (window.scrollY > limite) {
      bandeau.style.height = '100px';
      if (menu_actif) {
        menu.style.opacity = '0'; 
        menu_actif = false;
      }
    } else {
      bandeau.style.height = '150px';
      if (menu_actif) {
        menu.style.opacity = '1'; 
        menu_actif = true;
      }
    }
  });


  window.addEventListener('scroll', function() {
    var fleche = document.querySelector('.fleche');
    var texte = document.querySelector('h4');
    var limite = 110;
    var fleche_active = true;
    var texte_actif = true;

  
    if (window.scrollY > limite) {
        fleche.style.opacity = '0';
        texte.style.opacity ='0';
        fleche_active = false;
        texte_actif = false;
      
    } else {
        fleche.style.opacity = '1'; 
        texte.style.opacity = '1';
        fleche_active = true;
        texte_actif = true;
      }
  });



  function afficherMessage() {
    var prenom = document.getElementById("Prénom").value;
    var nom = document.getElementById("Nom").value;
    var email = document.getElementById("Email").value;
    var mfav = document.getElementById("Mfav").value;
    var ffav = document.getElementById("Ffav").value;
    var genre = document.getElementById("Genre").value;
    var commentaire = document.getElementById("commentaire").value;
    var newsletter = document.getElementById("option1").checked || document.getElementById("option2").checked;
  
    if (prenom && nom && email && newsletter) {
      alert("Merci d'avoir rempli le formulaire. Bienvenue chez Blabla !");
    } else {
      alert("Veuillez remplir tous les champs obligatoires du formulaire.");
    }
  }