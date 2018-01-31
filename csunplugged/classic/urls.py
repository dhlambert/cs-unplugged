"""URL redirect routing for the Classic CS Unplugged website."""

from django.conf.urls import url
from classic.views import redirect_to_classic_unplugged
from general.views import (
    GeneralIndexView,
    GeneralContactView,
)


urlpatterns = [
    url(
        r"^activities$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^artificial-intelligence$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^binary-numbers$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^books$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^changelog$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^class-simulation-computer-unfinished$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^community$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^community-activties$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^contact-us/$",
        GeneralContactView.as_view(),
    ),
    url(
        r"^contribute$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^cryptographic-protocols$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^curriculum-links$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^databases$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^divideandconquer$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^dominating-sets$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^error-detection$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^events$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^finite-state-automata$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^graph-colouring$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^harold-the-robot-2$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^human-interface-design$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^image-representation$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^information-hiding$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^information-theory$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^line-drawing$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^minimal-spanning-trees$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^modems-unplugged-2$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^network-protocols$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^people$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^phylogenetics$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^principles$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^programming-languages$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^projects$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^promotional$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^public-key-encryption$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^research$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^routing-and-deadlock$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^scout-patrol-encryption$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^searching-algorithms$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^sneak-peek/$",
        GeneralIndexView.as_view(),
    ),
    url(
        r"^sorting-algorithms$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^sorting-networks$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^steiner-trees$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^teachers$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^text-compression$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^the-turing-test$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^translations$",
        redirect_to_classic_unplugged,
    ),
    url(
        r"^videos$",
        redirect_to_classic_unplugged,
    ),
]
