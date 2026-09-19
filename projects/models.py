from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web", "Application web"),
        ("mobile", "Application mobile"),
        ("logiciel", "Logiciel de gestion"),
        ("vitrine", "Site vitrine"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField()
    technologies = models.CharField(
        max_length=300,
        help_text="Exemple : Django, Python, SQLite"
    )
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )
    link = models.URLField(
        blank=True,
        null=True
    )
    is_featured = models.BooleanField(
        default=True,
        verbose_name="Afficher sur l'accueil"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title