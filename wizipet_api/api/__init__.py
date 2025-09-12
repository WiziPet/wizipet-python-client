# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wizipet_api.api.front_account_api import FrontAccountApi
    from wizipet_api.api.front_accueil_api import FrontAccueilApi
    from wizipet_api.api.front_ads_api import FrontAdsApi
    from wizipet_api.api.front_alerte_perte_api import FrontAlertePerteApi
    from wizipet_api.api.front_antiparasitaire_api import FrontAntiparasitaireApi
    from wizipet_api.api.front_auth_api import FrontAuthApi
    from wizipet_api.api.front_carte_api import FrontCarteApi
    from wizipet_api.api.front_coaching_api import FrontCoachingApi
    from wizipet_api.api.front_contact_api import FrontContactApi
    from wizipet_api.api.front_discussion_api import FrontDiscussionApi
    from wizipet_api.api.front_encyclopedie_article_api import FrontEncyclopedieArticleApi
    from wizipet_api.api.front_encyclopedie_article_comment_api import FrontEncyclopedieArticleCommentApi
    from wizipet_api.api.front_group_api import FrontGroupApi
    from wizipet_api.api.front_historique_api import FrontHistoriqueApi
    from wizipet_api.api.front_medical_assistant_api import FrontMedicalAssistantApi
    from wizipet_api.api.front_notification_api import FrontNotificationApi
    from wizipet_api.api.front_pense_bete_api import FrontPenseBeteApi
    from wizipet_api.api.front_profile_api import FrontProfileApi
    from wizipet_api.api.front_promenade_api import FrontPromenadeApi
    from wizipet_api.api.front_publication_api import FrontPublicationApi
    from wizipet_api.api.front_publication_comment_api import FrontPublicationCommentApi
    from wizipet_api.api.front_rappel_api import FrontRappelApi
    from wizipet_api.api.front_sante_api import FrontSanteApi
    from wizipet_api.api.front_shopping_api import FrontShoppingApi
    from wizipet_api.api.front_vaccin_api import FrontVaccinApi
    from wizipet_api.api.front_vermifuge_api import FrontVermifugeApi
    from wizipet_api.api.front_version_api import FrontVersionApi
    from wizipet_api.api.front_warn_api import FrontWarnApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wizipet_api.api.front_account_api import FrontAccountApi
from wizipet_api.api.front_accueil_api import FrontAccueilApi
from wizipet_api.api.front_ads_api import FrontAdsApi
from wizipet_api.api.front_alerte_perte_api import FrontAlertePerteApi
from wizipet_api.api.front_antiparasitaire_api import FrontAntiparasitaireApi
from wizipet_api.api.front_auth_api import FrontAuthApi
from wizipet_api.api.front_carte_api import FrontCarteApi
from wizipet_api.api.front_coaching_api import FrontCoachingApi
from wizipet_api.api.front_contact_api import FrontContactApi
from wizipet_api.api.front_discussion_api import FrontDiscussionApi
from wizipet_api.api.front_encyclopedie_article_api import FrontEncyclopedieArticleApi
from wizipet_api.api.front_encyclopedie_article_comment_api import FrontEncyclopedieArticleCommentApi
from wizipet_api.api.front_group_api import FrontGroupApi
from wizipet_api.api.front_historique_api import FrontHistoriqueApi
from wizipet_api.api.front_medical_assistant_api import FrontMedicalAssistantApi
from wizipet_api.api.front_notification_api import FrontNotificationApi
from wizipet_api.api.front_pense_bete_api import FrontPenseBeteApi
from wizipet_api.api.front_profile_api import FrontProfileApi
from wizipet_api.api.front_promenade_api import FrontPromenadeApi
from wizipet_api.api.front_publication_api import FrontPublicationApi
from wizipet_api.api.front_publication_comment_api import FrontPublicationCommentApi
from wizipet_api.api.front_rappel_api import FrontRappelApi
from wizipet_api.api.front_sante_api import FrontSanteApi
from wizipet_api.api.front_shopping_api import FrontShoppingApi
from wizipet_api.api.front_vaccin_api import FrontVaccinApi
from wizipet_api.api.front_vermifuge_api import FrontVermifugeApi
from wizipet_api.api.front_version_api import FrontVersionApi
from wizipet_api.api.front_warn_api import FrontWarnApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
