# Présentation de Perl et Ruby

## Perl

### Introduction

**Perl** (Practical Extraction and Report Language) est un langage de programmation dynamique et interprété, créé par Larry Wall en 1987. Il est particulièrement bien adapté à la manipulation de texte et à l'extraction de données, mais il est également utilisé pour le développement web, l'administration système, la bioinformatique et bien d'autres domaines.

### Caractéristiques Principales

- **Manipulation de Texte** : Perl est connu pour ses puissantes capacités de manipulation de texte, notamment grâce à ses expressions régulières (regex) avancées.
- **Flexibilité et Extensibilité** : Perl permet d'écrire du code de différentes manières, offrant une grande flexibilité aux développeurs.
- **CPAN** : Le Comprehensive Perl Archive Network (CPAN) est un vaste référentiel de modules et de bibliothèques, facilitant l'extension des fonctionnalités de Perl.
- **Compatibilité** : Perl est très portable et fonctionne sur de nombreux systèmes d'exploitation.

### Exemple de Code

```perl
#!/usr/bin/perl
use strict;
use warnings;

# Exemple de script Perl
print "Bonjour, monde!\n";

# Manipulation de texte
my $texte = "Perl est puissant.";
$texte =~ s/p2uiss/puiss/i;  # Remplacement de texte avec regex
print "$texte\n";

# Lire un fichier
open(my $fh, '<', 'exemple.txt') or die "Impossible d'ouvrir le fichier: $!";
while (my $ligne = <$fh>) {
    print $ligne;
}
close($fh);
```

# Utilisations Courantes

 - Traitement de texte et extraction de données
 - Scripts d'administration système
 - Développement web avec frameworks comme Catalyst ou Dancer
 - Bioinformatique et analyse de données

## Ruby
### Introduction

Ruby est un langage de programmation dynamique, interprété, orienté objet, créé par Yukihiro "Matz" Matsumoto et publié pour la première fois en 1995. Ruby est conçu pour être simple à utiliser et productif, en mettant l'accent sur l'élégance et la lisibilité du code.
Caractéristiques Principales

   - Simplicité et Productivité : Ruby est conçu pour être facile à lire et à écrire, favorisant une syntaxe naturelle et concise.
   - Orienté Objet : En Ruby, tout est objet, ce qui permet une approche unifiée de la programmation.
   - Ruby on Rails : Un framework web populaire et puissant qui a contribué à la popularité de Ruby pour le développement web.
   - Métaprogrammation : Ruby supporte la métaprogrammation, permettant de définir des méthodes et des classes à la volée.

### Exemple de Code

```ruby

# Exemple de script Ruby
puts "Bonjour, monde!"

# Manipulation de texte
texte = "Ruby est élégant."
texte.gsub!('élégant', 'puissant')
puts texte

# Lire un fichier
File.open('exemple.txt', 'r') do |file|
  file.each_line do |line|
    puts line
  end
end
```

### Utilisations Courantes

   - Développement web avec Ruby on Rails
   - Automatisation de tâches
   - Développement d'applications de bureau et de scripts


Perl et Ruby sont deux langages dynamiques et interprétés avec des caractéristiques uniques. Perl excelle dans la manipulation de texte et les tâches d'administration système, tandis que Ruby se distingue par sa simplicité, sa productivité et son framework web Ruby on Rails. Chacun de ces langages a sa propre communauté et écosystème, offrant de nombreux modules et bibliothèques pour étendre leurs fonctionnalités. Le choix entre Perl et Ruby dépendra des besoins spécifiques du projet et des préférences personnelles du développeur.
