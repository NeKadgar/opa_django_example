from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AccessTag(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    access_tags = models.ManyToManyField(AccessTag, blank=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'is_default'],
                condition=models.Q(is_default=True),
                name='unique_default_team_per_company'
            )
        ]

    def __str__(self):
        return self.name


class AbstractCompanyModel(models.Model):
    access_tags = models.ManyToManyField(AccessTag, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        abstract = True
