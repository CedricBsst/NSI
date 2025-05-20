#  Devoir 4 - Réseaux

*Cet exercice porte sur les réseaux et les protocole de routage*

Un extrait de l'architecture réseau d'un ensemble scolaire "Établissement" est présenté ci-dessous. Plusieurs sites de cet établissement y sont présentés : l'administration, l'école primaire, le collège, le lycée général et le lycée professionnel. Les différents postes de ce réseau son reliés entre eux par des commutateurs (switchs) eux-même reliés à des routeurs.

Au sein de ce réseau, R1, R2, R3, R4, R5 et R6 correspondent aux routeurs de l'établissement.

![DS401](./DS%204_01.png)

> **Rappels :**
>
> - Une adresse IPv4 est compsé de 4 octets, soit 32 bits. Elle est notée A.B.C.D où A, B, C et D représentent les 4 octets de l'adresse.
> - La notation A.B.C.D/n signifie que les n premiers bits de l’adresse IP représentent la partie « réseau », les bits qui suivent représentent la partie « hôte ». Les n premier bits du masque sont donc égaux à 1 et les autres à 0.
> - L’adresse IPv4 dont tous les bits de la partie « hôte » sont à 0 est appelée « adresse du réseau ».
> - L’adresse IPv4 dont tous les bits de la partie « hôte » sont à 1 est appelée « adresse de diffusion ».

Le poste PC LG 03 de la salle informatique du lycée général a pour adresse IPv4 : 192.168.162.4. On donne ci-dessous le début de l’écriture binaire de cette adresse.
1. Recopier et compléter cette adresse IP : 1100 0000.1010 1000.xxxx xxxx.xxxx xxxx
2. Le poste PC Admin 02 du secteur « Administration »  a pour adresse IPv4 : 192.168.16.12/24
    - (a) Donner l’adresse du réseau local dédié au secteur « Administration » et son masque de sous-réseau.
    - (b) Donner l’adresse de diffusion (appelée aussi broadcast) de ce réseau.
    - (c) Donner le nombre maximal de machines que l’on peut connecter sur ce réseau.
3. L’administrateur réseau s’intéresse désormais à la performance des protocoles de routage au sein de l’établissement. En particulier, il porte son attention sur la transmission de paquets de données numériques du secteur « Administration » vers le secteur « Collège ».

    Son analyse portera donc sur les chemins entre les routeurs R6 et R3.

    Le protocole RIP (Routing Information Protocol) permet de construire les tables de routage des différents routeurs, en indiquant pour chaque routeur la distance, en nombre de saut, qui le sépare des autres routeurs

    - (a) On donne ci-dessous les tables de routages des routeurs R1, R2, R3 et R4 obtenues à l'aide de ce protocole.
        
        Donner les tables de routages des routeurs R5 et R6.

        ![DS4_O2](./DS%204_02.png)
    
    On souhaite transmettre un paquet de données depuis le poste PC Admin 01 vers le poste PC CLG 01.

    - (b) Déterminer le parcours emprunté par ce paquet, en utilisant les tables de routages données précédemment.
    - (c) Suite à une panne, le routeur R4 est déconnecté. Déterminer alors une nouvelle route pouvant être emprunté par les données depuis le secteur « Administration » vers le Collège en effectuant le moins de saut possibles.

4. Le routeur R4 est réparé et reconnecté au réseau.

    On applique désormais le protocole de routage OSPF (Open Shortest Path First) attribuant un coût à chaque liaison afin de privilégier le choix de certaines routes plus rapides.

    Le coût d’une liaison est défini par la relation : 

    $cout = \frac{10^8}{d}$

    - (a) Recopier et compléter le tableau suivant :

    |Liaison|Débit|Coût|
    |-|-|-|
    |Ethernet||$10$|
    |FAST-Ethernet|$10^8$||
    |Fibre|$10^9$||

    - (b) Recopier les schéma ci-dessous et indiquer le coût de chacune des liaisons connues.

    ![DS4_03](./DS%204_03.png)

    On sait que le parcours R6-R4-R5-R2 a un coût de $11,1$.

    - (c) Déterminer le type de liaison entre R6 et R4

    On souhaite acheminer un paquet de données depuis le secteur Administration vers le réseau du Lycée Général en utilisant le protocole OSPF.

    - (d) Déterminer alors la route empruntée par un paquet de données pour allet du poste PC Admin 01 vers le poste PC LG 01.