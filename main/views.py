from django.shortcuts import render, redirect
from .models import Mod, Category, Version
from django.views import View
from django.core.paginator import Paginator
import json


def sort_versions(versions):
    sorted_versions = [str(x[1]) for x in enumerate(versions)]
    for i in range(len(sorted_versions) - 1):
        for j in range(len(sorted_versions) - i - 1):
            cur = sorted_versions[j][2:].split(".")
            next = sorted_versions[j + 1][2:].split(".")
            if int(cur[0]) < int(next[0]):
                sorted_versions[j], sorted_versions[j + 1] = sorted_versions[j + 1], sorted_versions[j]
            elif int(cur[0]) == int(next[0]):
                if int(cur[1]) < int(next[1]):
                    sorted_versions[j], sorted_versions[j + 1] = sorted_versions[j + 1], sorted_versions[j]
    return sorted_versions

def filter_mods(mods, selected_version, selected_categories):
    temp_mods = []
    if selected_categories != []:
        for mod in mods:
            if mod.version.version == selected_version:
                    mod_categories = [mod_category[1].name for mod_category in list(enumerate(mod.categories.all()))]
                    if all(map(lambda category: category in mod_categories, selected_categories)):
                        temp_mods.append(mod)
            else:
                mod_categories = [mod_category[1].name for mod_category in list(enumerate(mod.categories.all()))]
                if all(map(lambda category: category in mod_categories, selected_categories)):
                        temp_mods.append(mod)
    else:
        for mod in mods:
            if mod.version.version == selected_version or selected_version == None:
                temp_mods.append(mod)
    return temp_mods

def redirect_to_page(request):
    return redirect("/page/1")


class ModListView(View):
    template_name = "main/html/modlist.html"

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        versions = sort_versions(Version.objects.all())
        selected_version = request.COOKIES.get('version', '')
        selected_categories = request.COOKIES.get('categories', '[]')
        selected_categories = json.loads(selected_categories)
        # selected_version = request.GET.get("version")
        # selected_categories = request.GET.getlist("categories")
        cur_page = int(kwargs["pk"])
        
        mods = filter_mods(Mod.objects.all(), selected_version, selected_categories)
        paginator = Paginator(mods, 5)
        mods_in_page = paginator.get_page(cur_page)

        return render(request, self.template_name, {
            "categories": categories,
            "versions": versions,
            "mods": mods_in_page,
            "cur_page": cur_page
        })
    
    def post(self, request, *args, **kwargs):
        # Обработка POST-запроса
        categories = Category.objects.all()
        versions = sort_versions(Version.objects.all())
        selected_version = request.COOKIES.get('version', '')
        selected_categories = request.COOKIES.get('categories', '[]')
        selected_categories = json.loads(selected_categories)
        cur_page = 1  # При POST-запросе всегда перекидываем на первую страницу

        mods = filter_mods(Mod.objects.all(), selected_version, selected_categories)
        paginator = Paginator(mods, 5)
        mods_in_page = paginator.get_page(cur_page)


        return render(request, self.template_name, {
            "categories": categories,
            "versions": versions,
            "mods": mods_in_page,
            "cur_page": cur_page
        })
