from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Company, Advantage, Review

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

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
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        if name and email and content:
            comment = Comment(post=post, name=name, email=email, content=content)
            comment.save()
    return redirect('post_detail', pk=post_id)

def company_ratings(request):
    companies = Company.objects.all()
    return render(request, 'blog/companies.html', {'companies': companies})

def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    reviews = company.reviews.all()

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

    return render(request, 'blog/company_detail.html', {'company': company, 'reviews': reviews})


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
    print(3)
    advantage = get_object_or_404(Advantage, pk=advantage_id)
    advantage.count += 1
    advantage.save()
    return redirect('company_detail', company_id=advantage.company.id)

