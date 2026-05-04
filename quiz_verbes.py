import customtkinter as ctk
import random
import re
import unicodedata
import json
import os

# Base de données complète de tes 146 verbes
verbes = [
    {"inf": "awake", "pret": "awoke", "pp": "awoken", "trad": "(se) réveiller"},
    {"inf": "be", "pret": "was/were", "pp": "been", "trad": "être"},
    {"inf": "bear", "pret": "bore", "pp": "borne", "trad": "porter/supporter/soutenir"},
    {"inf": "beat", "pret": "beat", "pp": "beaten", "trad": "battre"},
    {"inf": "become", "pret": "became", "pp": "become", "trad": "devenir"},
    {"inf": "begin", "pret": "began", "pp": "begun", "trad": "commencer"},
    {"inf": "bend", "pret": "bent", "pp": "bent", "trad": "se courber"},
    {"inf": "bet", "pret": "bet", "pp": "bet", "trad": "parier"},
    {"inf": "bid", "pret": "bade", "pp": "bidden", "trad": "ordonner"},
    {"inf": "bind", "pret": "bound", "pp": "bound", "trad": "lier"},
    {"inf": "bite", "pret": "bit", "pp": "bitten", "trad": "mordre"},
    {"inf": "bleed", "pret": "bled", "pp": "bled", "trad": "saigner"},
    {"inf": "blow", "pret": "blew", "pp": "blown", "trad": "souffler"},
    {"inf": "break", "pret": "broke", "pp": "broken", "trad": "casser"},
    {"inf": "breed", "pret": "bred", "pp": "bred", "trad": "élever"},
    {"inf": "bring", "pret": "brought", "pp": "brought", "trad": "apporter"},
    {"inf": "build", "pret": "built", "pp": "built", "trad": "construire"},
    {"inf": "burn", "pret": "burnt", "pp": "burnt", "trad": "brûler"},
    {"inf": "burst", "pret": "burst", "pp": "burst", "trad": "éclater"},
    {"inf": "buy", "pret": "bought", "pp": "bought", "trad": "acheter"},
    {"inf": "cast", "pret": "cast", "pp": "cast", "trad": "jeter"},
    {"inf": "catch", "pret": "caught", "pp": "caught", "trad": "attraper"},
    {"inf": "choose", "pret": "chose", "pp": "chosen", "trad": "choisir"},
    {"inf": "cling", "pret": "clung", "pp": "clung", "trad": "se cramponner"},
    {"inf": "come", "pret": "came", "pp": "come", "trad": "venir"},
    {"inf": "cost", "pret": "cost", "pp": "cost", "trad": "coûter"},
    {"inf": "creep", "pret": "crept", "pp": "crept", "trad": "ramper/se glisser/se hérisser"},
    {"inf": "cut", "pret": "cut", "pp": "cut", "trad": "couper"},
    {"inf": "deal", "pret": "dealt", "pp": "dealt", "trad": "distribuer/traiter"},
    {"inf": "dig", "pret": "dug", "pp": "dug", "trad": "bêcher"},
    {"inf": "do", "pret": "did", "pp": "done", "trad": "faire"},
    {"inf": "draw", "pret": "drew", "pp": "drawn", "trad": "tirer/dessiner"},
    {"inf": "dream", "pret": "dreamt", "pp": "dreamt", "trad": "rêver"},
    {"inf": "drink", "pret": "drank", "pp": "drunk", "trad": "boire"},
    {"inf": "drive", "pret": "drove", "pp": "driven", "trad": "conduire"},
    {"inf": "dwell", "pret": "dwelt", "pp": "dwelt", "trad": "habiter/rester"},
    {"inf": "eat", "pret": "ate", "pp": "eaten", "trad": "manger"},
    {"inf": "fall", "pret": "fell", "pp": "fallen", "trad": "tomber"},
    {"inf": "feed", "pret": "fed", "pp": "fed", "trad": "nourrir"},
    {"inf": "feel", "pret": "felt", "pp": "felt", "trad": "(se) sentir"},
    {"inf": "fight", "pret": "fought", "pp": "fought", "trad": "combattre"},
    {"inf": "find", "pret": "found", "pp": "found", "trad": "trouver"},
    {"inf": "flee", "pret": "fled", "pp": "fled", "trad": "fuir"},
    {"inf": "fling", "pret": "flung", "pp": "flung", "trad": "jeter"},
    {"inf": "fly", "pret": "flew", "pp": "flown", "trad": "voler"},
    {"inf": "forbid", "pret": "forbade", "pp": "forbidden", "trad": "interdire"},
    {"inf": "forget", "pret": "forgot", "pp": "forgotten", "trad": "oublier"},
    {"inf": "forgive", "pret": "forgave", "pp": "forgiven", "trad": "pardonner"},
    {"inf": "freeze", "pret": "froze", "pp": "frozen", "trad": "geler"},
    {"inf": "get", "pret": "got", "pp": "got", "trad": "obtenir"},
    {"inf": "give", "pret": "gave", "pp": "given", "trad": "donner"},
    {"inf": "go", "pret": "went", "pp": "gone", "trad": "aller"},
    {"inf": "grind", "pret": "ground", "pp": "ground", "trad": "broyer/moudre"},
    {"inf": "grow", "pret": "grew", "pp": "grown", "trad": "cultiver/pousser/grandir"},
    {"inf": "hang", "pret": "hung", "pp": "hung", "trad": "pendre"},
    {"inf": "have", "pret": "had", "pp": "had", "trad": "avoir"},
    {"inf": "hear", "pret": "heard", "pp": "heard", "trad": "entendre"},
    {"inf": "hide", "pret": "hid", "pp": "hidden", "trad": "(se) cacher"},
    {"inf": "hit", "pret": "hit", "pp": "hit", "trad": "frapper"},
    {"inf": "hold", "pret": "held", "pp": "held", "trad": "tenir"},
    {"inf": "hurt", "pret": "hurt", "pp": "hurt", "trad": "nuire"},
    {"inf": "keep", "pret": "kept", "pp": "kept", "trad": "garder"},
    {"inf": "kneel", "pret": "knelt", "pp": "knelt", "trad": "s'agenouiller"},
    {"inf": "knit", "pret": "knit", "pp": "knit", "trad": "tricoter"},
    {"inf": "know", "pret": "knew", "pp": "known", "trad": "savoir/connaître"},
    {"inf": "lay", "pret": "laid", "pp": "laid", "trad": "étendre/coucher"},
    {"inf": "lead", "pret": "led", "pp": "led", "trad": "mener"},
    {"inf": "leap", "pret": "leapt", "pp": "leapt", "trad": "sauter/bondir"},
    {"inf": "learn", "pret": "learnt", "pp": "learnt", "trad": "apprendre"},
    {"inf": "leave", "pret": "left", "pp": "left", "trad": "quitter/laisser"},
    {"inf": "lend", "pret": "lent", "pp": "lent", "trad": "prêter"},
    {"inf": "let", "pret": "let", "pp": "let", "trad": "laisser/louer"},
    {"inf": "lie", "pret": "lay", "pp": "lain", "trad": "reposer/être couché"},
    {"inf": "light", "pret": "lit", "pp": "lit", "trad": "allumer"},
    {"inf": "lose", "pret": "lost", "pp": "lost", "trad": "perdre"},
    {"inf": "make", "pret": "made", "pp": "made", "trad": "faire"},
    {"inf": "mean", "pret": "meant", "pp": "meant", "trad": "vouloir dire/signifier"},
    {"inf": "meet", "pret": "met", "pp": "met", "trad": "rencontrer"},
    {"inf": "mow", "pret": "mowed", "pp": "mown", "trad": "faucher/tondre"},
    {"inf": "pay", "pret": "paid", "pp": "paid", "trad": "payer"},
    {"inf": "prove", "pret": "proved", "pp": "proven", "trad": "prouver"},
    {"inf": "put", "pret": "put", "pp": "put", "trad": "mettre"},
    {"inf": "quit", "pret": "quit", "pp": "quit", "trad": "quitter/abandonner"},
    {"inf": "read", "pret": "read", "pp": "read", "trad": "lire"},
    {"inf": "rid", "pret": "rid", "pp": "ridden", "trad": "se débarrasser"},
    {"inf": "ride", "pret": "rode", "pp": "ridden", "trad": "monter"},
    {"inf": "ring", "pret": "rang", "pp": "rung", "trad": "sonner/résonner"},
    {"inf": "rise", "pret": "rose", "pp": "risen", "trad": "se lever"},
    {"inf": "run", "pret": "ran", "pp": "run", "trad": "courir"},
    {"inf": "saw", "pret": "sawed", "pp": "sawn", "trad": "scier"},
    {"inf": "say", "pret": "said", "pp": "said", "trad": "dire"},
    {"inf": "see", "pret": "saw", "pp": "seen", "trad": "voir"},
    {"inf": "seek", "pret": "sought", "pp": "sought", "trad": "chercher"},
    {"inf": "sell", "pret": "sold", "pp": "sold", "trad": "vendre"},
    {"inf": "send", "pret": "sent", "pp": "sent", "trad": "envoyer"},
    {"inf": "set", "pret": "set", "pp": "set", "trad": "mettre"},
    {"inf": "sew", "pret": "sewed", "pp": "sewn", "trad": "coudre"},
    {"inf": "shake", "pret": "shook", "pp": "shaken", "trad": "secouer"},
    {"inf": "shine", "pret": "shone", "pp": "shone", "trad": "briller"},
    {"inf": "shoot", "pret": "shot", "pp": "shot", "trad": "tirer/tuer par balle/filmer"},
    {"inf": "show", "pret": "showed", "pp": "shown", "trad": "montrer"},
    {"inf": "shrink", "pret": "shrank", "pp": "shrunk", "trad": "(se) contracter/(se) rétrécir"},
    {"inf": "shut", "pret": "shut", "pp": "shut", "trad": "fermer"},
    {"inf": "sing", "pret": "sang", "pp": "sung", "trad": "chanter"},
    {"inf": "sink", "pret": "sank", "pp": "sunk", "trad": "enfoncer/couler"},
    {"inf": "sit", "pret": "sat", "pp": "sat", "trad": "s'asseoir"},
    {"inf": "sleep", "pret": "slept", "pp": "slept", "trad": "dormir"},
    {"inf": "slide", "pret": "slid", "pp": "slid", "trad": "glisser"},
    {"inf": "smell", "pret": "smelt", "pp": "smelt", "trad": "sentir/flairer"},
    {"inf": "sow", "pret": "sowed", "pp": "sown", "trad": "semer"},
    {"inf": "speak", "pret": "spoke", "pp": "spoken", "trad": "parler"},
    {"inf": "speed", "pret": "sped", "pp": "sped", "trad": "se presser"},
    {"inf": "spell", "pret": "spelt", "pp": "spelt", "trad": "épeler/orthographier"},
    {"inf": "spend", "pret": "spent", "pp": "spent", "trad": "dépenser"},
    {"inf": "spill", "pret": "spilt", "pp": "spilt", "trad": "(se) renverser/(se) répandre"},
    {"inf": "spin", "pret": "span", "pp": "spun", "trad": "faire tourner/filer"},
    {"inf": "spit", "pret": "spat", "pp": "spat", "trad": "cracher"},
    {"inf": "split", "pret": "split", "pp": "split", "trad": "(se) fendre"},
    {"inf": "spoil", "pret": "spoilt", "pp": "spoilt", "trad": "abimer/gâter"},
    {"inf": "spread", "pret": "spread", "pp": "spread", "trad": "étendre"},
    {"inf": "spring", "pret": "sprang", "pp": "sprung", "trad": "bondir"},
    {"inf": "stand", "pret": "stood", "pp": "stood", "trad": "être debout"},
    {"inf": "steal", "pret": "stole", "pp": "stolen", "trad": "voler"},
    {"inf": "stick", "pret": "stuck", "pp": "stuck", "trad": "coller"},
    {"inf": "sting", "pret": "stung", "pp": "stung", "trad": "piquer/brûler"},
    {"inf": "stink", "pret": "stank", "pp": "stunk", "trad": "puer"},
    {"inf": "strike", "pret": "struck", "pp": "struck", "trad": "frapper/se mettre en grève"},
    {"inf": "strive", "pret": "strove", "pp": "striven", "trad": "s'efforcer"},
    {"inf": "swear", "pret": "swore", "pp": "sworn", "trad": "jurer"},
    {"inf": "sweep", "pret": "swept", "pp": "swept", "trad": "balayer"},
    {"inf": "swell", "pret": "swelled", "pp": "swollen", "trad": "gonfler"},
    {"inf": "swim", "pret": "swam", "pp": "swum", "trad": "nager"},
    {"inf": "swing", "pret": "swung", "pp": "swung", "trad": "balancer"},
    {"inf": "take", "pret": "took", "pp": "taken", "trad": "prendre"},
    {"inf": "teach", "pret": "taught", "pp": "taught", "trad": "enseigner"},
    {"inf": "tear", "pret": "tore", "pp": "torn", "trad": "déchirer"},
    {"inf": "tell", "pret": "told", "pp": "told", "trad": "raconter"},
    {"inf": "think", "pret": "thought", "pp": "thought", "trad": "penser"},
    {"inf": "thrive", "pret": "throve", "pp": "thriven", "trad": "prospérer"},
    {"inf": "throw", "pret": "threw", "pp": "thrown", "trad": "jeter"},
    {"inf": "understand", "pret": "understood", "pp": "understood", "trad": "comprendre"},
    {"inf": "wake", "pret": "woke", "pp": "woken", "trad": "(se) réveiller/(se) ranimer"},
    {"inf": "wear", "pret": "wore", "pp": "worn", "trad": "porter/user"},
    {"inf": "wet", "pret": "wet", "pp": "wet", "trad": "mouiller"},
    {"inf": "win", "pret": "won", "pp": "won", "trad": "gagner"},
    {"inf": "write", "pret": "wrote", "pp": "written", "trad": "écrire"}
]

FICHIER_STATS = "stats_erreurs.json"

# --- REGLAGE DU ZOOM POUR LES GRANDS ECRANS ---
ZOOM_GLOBAL = 2

# --- PALETTE DE COULEURS FAÇON QUIZLET ---
BG_PAGE = "#F6F7FB"        
BG_CARD = "#FFFFFF"        
TEXT_DARK = "#1A1D28"      
TEXT_LIGHT = "#5E6278"     
QUIZLET_BLUE = "#4255FF"   
QUIZLET_HOVER = "#3342CC"  
BTN_GREEN = "#23B08E"      
BTN_GREEN_HOVER = "#1C8D72"
BTN_ORANGE = "#FFC233"     
BTN_ORANGE_HOVER = "#E6AA2B"
BTN_RED = "#FF6B6B"
BTN_RED_HOVER = "#E55C5C"
BORDER_COLOR = "#D9DCE8"   

# Configuration CustomTkinter
ctk.set_appearance_mode("Light")
ctk.set_widget_scaling(ZOOM_GLOBAL)
ctk.set_window_scaling(ZOOM_GLOBAL)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Verbes Irréguliers")
        self.root.configure(fg_color=BG_PAGE)
        
        # Plein écran
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))

        # Conteneur principal centré
        self.main_container = ctk.CTkFrame(root, fg_color=BG_PAGE)
        self.main_container.pack(expand=True)

        self.verbes_restants = list(verbes)
        self.verbe_actuel = {}
        self.tentative_terminee = False 
        self.stats_erreurs = self.charger_stats()
        
        # --- EN-TÊTE ---
        self.lbl_compteur = ctk.CTkLabel(self.main_container, text=f"Verbes restants : {len(self.verbes_restants)}", 
                                     font=("Helvetica", 18, "bold"), text_color=TEXT_LIGHT)
        self.lbl_compteur.pack(pady=(0, 10))
        
        ctk.CTkLabel(self.main_container, text="Comment souhaitez-vous étudier ?", 
                 font=("Helvetica", 38, "bold"), text_color=TEXT_DARK).pack(pady=(0, 10))
        ctk.CTkLabel(self.main_container, text="Complétez les 3 cases vides pour maîtriser vos verbes.", 
                 font=("Helvetica", 20), text_color=TEXT_LIGHT).pack(pady=(0, 30))

        # --- CARTE BLANCHE ---
        self.card_frame = ctk.CTkFrame(self.main_container, fg_color=BG_CARD, corner_radius=20,
                                       border_color=BORDER_COLOR, border_width=2)
        self.card_frame.pack(pady=10, padx=20, ipadx=40, ipady=30)

        # Labels et Champs de texte
        self.ent_inf = self.creer_champ(self.card_frame, "Infinitif :", 0)
        self.ent_pret = self.creer_champ(self.card_frame, "Prétérit :", 1)
        self.ent_pp = self.creer_champ(self.card_frame, "Participe Passé :", 2)
        self.ent_trad = self.creer_champ(self.card_frame, "Traduction :", 3)

        # Messages de retour
        self.lbl_feedback = ctk.CTkLabel(self.main_container, text="", font=("Helvetica", 24, "bold"))
        self.lbl_feedback.pack(pady=20)

        # --- BOUTONS ---
        self.frame_btns = ctk.CTkFrame(self.main_container, fg_color=BG_PAGE)
        self.frame_btns.pack(pady=10)
        
        self.btn_valider = self.creer_bouton(self.frame_btns, "Valider (Entrée)", BTN_GREEN, BTN_GREEN_HOVER, self.valider_reponse, width=220)
        self.btn_valider.grid(row=0, column=0, padx=15)

        self.btn_suivant = self.creer_bouton(self.frame_btns, "Suivant (→)", QUIZLET_BLUE, QUIZLET_HOVER, self.generer_nouveau_verbe, width=220)
        self.btn_suivant.grid(row=0, column=1, padx=15)

        # Boutons secondaires
        self.btn_stats = self.creer_bouton(self.main_container, "📊 Statistiques d'erreurs", BTN_ORANGE, BTN_ORANGE_HOVER, self.afficher_stats, width=350, font_size=16)
        self.btn_stats.pack(pady=(25, 10))

        self.btn_quitter = self.creer_bouton(self.main_container, f"Quitter & Voir les {len(self.verbes_restants)} restants", BTN_RED, BTN_RED_HOVER, self.afficher_restants, width=350, font_size=16)
        self.btn_quitter.pack(pady=5)

        # Raccourcis
        self.root.bind('<Return>', lambda event: self.valider_reponse())
        self.root.bind('<Right>', lambda event: self.action_suivant_clavier())
        
        self.generer_nouveau_verbe()

    # --- FONCTIONS DE DESIGN CTK ---
    def creer_champ(self, parent, texte_label, ligne):
        ctk.CTkLabel(parent, text=texte_label, font=("Helvetica", 18, "bold"), text_color=TEXT_DARK).grid(row=ligne, column=0, sticky="e", pady=15, padx=20)
        ent = ctk.CTkEntry(parent, font=("Helvetica", 18), width=450, height=50, corner_radius=12, 
                           border_color=BORDER_COLOR, border_width=2, fg_color=BG_CARD, text_color=TEXT_DARK)
        ent.grid(row=ligne, column=1, pady=15, padx=15)
        return ent

    def creer_bouton(self, parent, texte, couleur_bg, couleur_hover, commande, width=200, font_size=18):
        btn = ctk.CTkButton(parent, text=texte, font=("Helvetica", font_size, "bold"), fg_color=couleur_bg, hover_color=couleur_hover, 
                            corner_radius=12, width=width, height=50, command=commande, cursor="hand2")
        return btn

    def desactiver_champ(self, champ, texte):
        champ.insert(0, texte)
        champ.configure(state="readonly", fg_color="#F0F2F5", text_color=TEXT_LIGHT)

    # --- GESTION DES FICHIERS STATS ---
    def charger_stats(self):
        if os.path.exists(FICHIER_STATS):
            with open(FICHIER_STATS, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def sauvegarder_stats(self):
        with open(FICHIER_STATS, "w", encoding="utf-8") as f:
            json.dump(self.stats_erreurs, f, indent=4, ensure_ascii=False)

    def ajouter_erreur(self, infinitif):
        if infinitif not in self.stats_erreurs:
            self.stats_erreurs[infinitif] = 0
        self.stats_erreurs[infinitif] += 1
        self.sauvegarder_stats()

    # --- LOGIQUE DU JEU ---
    def action_suivant_clavier(self):
        if self.tentative_terminee or len(self.verbes_restants) == 0:
            self.generer_nouveau_verbe()

    def generer_nouveau_verbe(self):
        if len(self.verbes_restants) == 0:
            self.lbl_feedback.configure(text="🎉 Félicitations ! Liste terminée !", text_color=BTN_GREEN)
            for champ in (self.ent_inf, self.ent_pret, self.ent_pp, self.ent_trad):
                champ.configure(state="normal")
                champ.delete(0, 'end')
                champ.configure(state="disabled")
            self.btn_valider.configure(state="disabled")
            self.btn_suivant.configure(state="disabled")
            self.btn_quitter.configure(text="Quitter l'application")
            return

        self.tentative_terminee = False
        self.btn_valider.configure(state="normal", fg_color=BTN_GREEN)
        self.lbl_feedback.configure(text="")
        
        self.verbe_actuel = random.choice(self.verbes_restants)
        cle_indice = random.choice(["inf", "pret", "pp", "trad"])

        for champ in (self.ent_inf, self.ent_pret, self.ent_pp, self.ent_trad):
            champ.configure(state="normal", fg_color=BG_CARD, text_color=TEXT_DARK)
            champ.delete(0, 'end')

        if cle_indice == "inf":
            self.desactiver_champ(self.ent_inf, self.verbe_actuel["inf"])
            self.ent_pret.focus()
        elif cle_indice == "pret":
            self.desactiver_champ(self.ent_pret, self.verbe_actuel["pret"])
            self.ent_inf.focus()
        elif cle_indice == "pp":
            self.desactiver_champ(self.ent_pp, self.verbe_actuel["pp"])
            self.ent_inf.focus()
        else:
            self.desactiver_champ(self.ent_trad, self.verbe_actuel["trad"])
            self.ent_inf.focus()

    def supprimer_accents(self, texte):
        texte_normalise = unicodedata.normalize('NFD', texte)
        return "".join(c for c in texte_normalise if unicodedata.category(c) != 'Mn')

    def verifier_mot(self, reponse_user, reponse_attendue):
        reponse_user = " ".join(reponse_user.strip().lower().split())
        reponse_user = self.supprimer_accents(reponse_user)
        options_valides = []
        
        phrase_complete = " ".join(reponse_attendue.strip().lower().split())
        options_valides.append(self.supprimer_accents(phrase_complete))
        
        options_brutes = [opt.strip().lower() for opt in reponse_attendue.split('/')]
        for opt in options_brutes:
            opt_exact = " ".join(opt.split())
            options_valides.append(self.supprimer_accents(opt_exact))
            
            opt_avec_parenth = opt.replace('(', '').replace(')', '')
            opt_avec_parenth = " ".join(opt_avec_parenth.split())
            options_valides.append(self.supprimer_accents(opt_avec_parenth))
            
            opt_sans_parenth = re.sub(r'\(.*?\)', '', opt)
            opt_sans_parenth = " ".join(opt_sans_parenth.split())
            options_valides.append(self.supprimer_accents(opt_sans_parenth))

        return reponse_user in options_valides

    def valider_reponse(self):
        if self.tentative_terminee or len(self.verbes_restants) == 0:
            return

        self.tentative_terminee = True
        self.btn_valider.configure(state="disabled", fg_color="#A0A0A0") 

        for champ in (self.ent_inf, self.ent_pret, self.ent_pp, self.ent_trad):
            if str(champ.cget("state")) != "readonly":
                champ.configure(state="readonly", fg_color="#FAFAFA")

        rep_inf = self.ent_inf.get()
        rep_pret = self.ent_pret.get()
        rep_pp = self.ent_pp.get()
        rep_trad = self.ent_trad.get()

        if (self.verifier_mot(rep_inf, self.verbe_actuel["inf"]) and
            self.verifier_mot(rep_pret, self.verbe_actuel["pret"]) and
            self.verifier_mot(rep_pp, self.verbe_actuel["pp"]) and
            self.verifier_mot(rep_trad, self.verbe_actuel["trad"])):
            
            self.lbl_feedback.configure(text="✅ Excellent !", text_color=BTN_GREEN)
            self.verbes_restants.remove(self.verbe_actuel)
            
            self.lbl_compteur.configure(text=f"Verbes restants : {len(self.verbes_restants)}")
            if len(self.verbes_restants) > 0:
                self.btn_quitter.configure(text=f"Quitter & Voir les {len(self.verbes_restants)} restants")
            else:
                self.btn_quitter.configure(text="Quitter l'application")
        else:
            self.lbl_feedback.configure(
                text=f"❌ Faux.\nCorrection : {self.verbe_actuel['inf']} - {self.verbe_actuel['pret']} - {self.verbe_actuel['pp']}\nTrad : {self.verbe_actuel['trad']}",
                text_color=BTN_RED
            )
            self.ajouter_erreur(self.verbe_actuel["inf"])

    # --- FENÊTRES SECONDAIRES ---
    def afficher_stats(self):
        fenetre_stats = ctk.CTkToplevel(self.root)
        fenetre_stats.title("Historique des erreurs")
        fenetre_stats.geometry("600x800") 
        fenetre_stats.configure(fg_color=BG_PAGE)
        fenetre_stats.attributes('-topmost', 'true')
        
        ctk.CTkLabel(fenetre_stats, text="Verbes les plus ratés", font=("Helvetica", 28, "bold"), text_color=TEXT_DARK).pack(pady=25)
        
        text_widget = ctk.CTkTextbox(fenetre_stats, font=("Helvetica", 20), fg_color=BG_CARD, 
                                     text_color=TEXT_DARK, corner_radius=15, border_color=BORDER_COLOR, border_width=1)
        text_widget.pack(expand=True, fill="both", padx=30, pady=15)
        
        stats_triees = sorted(self.stats_erreurs.items(), key=lambda item: item[1], reverse=True)
        
        if not stats_triees:
            texte_final = "\n\n🎉 Aucune erreur enregistrée !\nContinue comme ça !"
        else:
            texte_final = "\n\n".join(f"  ❌ {verbe} : {erreurs} erreur(s)" for verbe, erreurs in stats_triees)
        
        text_widget.insert('end', texte_final)
        text_widget.configure(state="disabled")
        
        self.creer_bouton(fenetre_stats, "Fermer", TEXT_LIGHT, TEXT_DARK, fenetre_stats.destroy, width=300).pack(pady=25)

    def afficher_restants(self):
        if len(self.verbes_restants) == 0:
            self.root.destroy()
            return

        fenetre_fin = ctk.CTkToplevel(self.root)
        fenetre_fin.title("Bilan de session")
        fenetre_fin.geometry("600x800") 
        fenetre_fin.configure(fg_color=BG_PAGE)
        fenetre_fin.attributes('-topmost', 'true')
        
        ctk.CTkLabel(fenetre_fin, text=f"Il te reste {len(self.verbes_restants)} verbes", font=("Helvetica", 28, "bold"), text_color=TEXT_DARK).pack(pady=25)
        
        text_widget = ctk.CTkTextbox(fenetre_fin, font=("Helvetica", 20), fg_color=BG_CARD, 
                                     text_color=TEXT_DARK, corner_radius=15, border_color=BORDER_COLOR, border_width=1)
        text_widget.pack(expand=True, fill="both", padx=30, pady=15)
        
        liste_infinitifs = sorted([v['inf'] for v in self.verbes_restants])
        texte_final = "\n".join(f"  • {inf}" for inf in liste_infinitifs)
        
        text_widget.insert('end', texte_final)
        text_widget.configure(state="disabled")
        
        self.creer_bouton(fenetre_fin, "Fermer le programme", BTN_RED, BTN_RED_HOVER, self.root.destroy, width=300).pack(pady=25)

if __name__ == "__main__":
    racine = ctk.CTk()
    app = QuizApp(racine)
    racine.mainloop()