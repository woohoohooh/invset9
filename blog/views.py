from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Company, Advantage, Review, Guides, About, SecurityScore, Category
from django.db.models import Sum, Avg,  F, Sum
from django.db import transaction


def guides(request):
    guides = Guides.objects.all()
    return render(request, 'blog/guides.html', {'guides': guides, 'request': request})

def about(request):
    about = About.objects.first()
    return render(request, 'blog/about.html', {'about': about, 'request': request})

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'request': request})

def company_ratings(request):
    companies = Company.objects.all()
    return render(request, 'blog/companies.html', {'companies': companies, 'request': request})

def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()
        return redirect('post_detail', pk=post.id)
    else:
        return render(request, 'blog/post_create.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/post_detail.html', context)

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        if name and content:
            comment = Comment(post=post, name=name, content=content)
            comment.save()
    return redirect('post_detail', pk=post_id)

def calculate_total_score(company):
    security_scores = company.securityscore_set.first()
    asset_secured_score = security_scores.asset_secured_score
    emission_limit_score = security_scores.emission_limit_score
    liquidity_score = security_scores.liquidity_score
    total_score = (asset_secured_score + emission_limit_score + liquidity_score) / 3
    security_scores.total_score = total_score
    security_scores.save()

    team_scores = company.teamscore_set.first()
    decentralized_score = team_scores.decentralized_score
    performace_score = team_scores.performace_score
    total_score = (decentralized_score + performace_score) / 2
    team_scores.total_score = total_score
    team_scores.save()

    product_scores = company.productscore_set.first()
    performace_score = product_scores.performace_score
    apy_1yr_score = product_scores.apy_1yr_score
    apy_5yr_score = product_scores.apy_5yr_score
    total_score = (performace_score + apy_1yr_score + apy_5yr_score) / 3
    product_scores.total_score = total_score
    product_scores.save()

def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    reviews = company.reviews.all()

    security_advantages = company.advantages.filter(position=1).order_by('-count')
    team_advantages = company.advantages.filter(position=2).order_by('-count')
    product_advantages = company.advantages.filter(position=3).order_by('-count')

    calculate_total_score(company)

    security_scores = company.securityscore_set.first()
    team_scores = company.teamscore_set.first()
    product_scores = company.productscore_set.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')

        if rating == 'positive':
            rating = True
        elif rating == 'negative':
            rating = False

        review = Review(company=company, name=name, rating=rating, comment=comment)
        review.save()
        return redirect('company_detail', company_id=company.id)

    return render(request, 'blog/company_detail.html', {'company': company, 'reviews': reviews, 'security_advantages': security_advantages, 'team_advantages': team_advantages, 'product_advantages': product_advantages, 'security_scores': security_scores, 'team_scores': team_scores, 'product_scores': product_scores})

def add_advantage(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        position = request.POST.get('position')
        advantage = request.POST.get('advantage')
        mark = request.POST.get('mark')
        count = 1  # Установите значение по умолчанию для поля count

        if mark == 'positive':
            mark = True
        elif mark == 'negative':
            mark = False

        if advantage and position:
            advantage = Advantage.objects.create(
                company=company,
                position=position,
                advantage=advantage,
                mark=mark,
                count=count)  # Передайте значение count при создании объекта
            advantage.save()

    return redirect('company_detail', company_id=company_id)

def increment_advantage(request, advantage_id):
    advantage = get_object_or_404(Advantage, pk=advantage_id)

    if request.method == 'POST':
        if advantage.position == 1 or advantage.position == 2 or advantage.position == 3:
            # Увеличение процента выбранного преимущества
            advantage.count += 1
            advantage.save()

            # Получение всех преимуществ в столбце для данной компании
            advantages = Advantage.objects.filter(company=advantage.company, position=advantage.position)

            # Подсчет общего количества преимуществ в столбце
            total_count = advantages.aggregate(total_count=Sum('count'))['total_count']

            # Проверка, чтобы общий процент не превышал 100%
            if total_count > 100:
                advantages.update(count=F('count') * 100 / total_count)
                total_count = 100

            # Распределение процентов между преимуществами
            remaining_percent = 100 - total_count
            remaining_advantages = advantages.exclude(id=advantage.id)
            remaining_count = remaining_advantages.count()

            if remaining_count > 0:
                remaining_percent_per_advantage = remaining_percent / remaining_count

                for adv in remaining_advantages:
                    adv.count += remaining_percent_per_advantage
                    adv.save()

            # Проверка, чтобы общий процент равнялся 100%
            total_count = advantages.aggregate(total_count=Sum('count'))['total_count']
            if total_count < 100:
                remaining_percent = 100 - total_count
                advantage.count += remaining_percent
                advantage.save()

    return redirect('company_detail', company_id=advantage.company.id)