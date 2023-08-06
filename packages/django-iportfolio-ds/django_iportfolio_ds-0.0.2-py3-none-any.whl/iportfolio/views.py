from django.shortcuts import render, get_object_or_404
from util_demian import utils
from _data import iportfolio_contents
from .models import Portfolio


import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.ERROR)

font_link = "https://fonts.googleapis.com/css?" \
            "family=Open+Sans:wght@300,300i,400,400i,600,600i,700,700i&" \
            "family=Hahmlet:wght@100;200;300;400;500;600;700;800;900&" \
            "family=Noto+Sans+KR:wght@100;300;400;500;700;900&" \
            "family=Noto+Serif+KR:wght@200;300;400;500;600;700;900&" \
            "family=Raleway:wght@300,300i,400,400i,500,500i,600,600i,700,700i&" \
            "family=Poppins:wght@300,300i,400,400i,500,500i,600,600i,700,700i&display=swap"


def robots(request):
    from django.shortcuts import HttpResponse
    file_content = utils.make_robots()
    return HttpResponse(file_content, content_type="text/plain")


def home(request):
    """
        컨텍스트를 이곳에서 만들지 않고 _data 폴더의 contents.py에서 만들어진 것을 가져다 쓴다.
        """
    c = iportfolio_contents.context

    # _variables.scss에서 한글 폰트를 추가해주고 여기에 적절한 폰트 링크를 적용한다.
    c['font_link'] = font_link

    logger.info(c)
    return render(request, 'iportfolio/index.html', c)


def details(request, id: int):
    c = iportfolio_contents.context
    c.update({'obj': get_object_or_404(Portfolio, pk=id)})
    logger.debug(c)
    return render(request, "iportfolio/_portfolio-details.html", c)
