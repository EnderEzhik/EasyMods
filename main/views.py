from django.shortcuts import render
from .models import Mod, Category, Version


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

def filter_mods(mods, version, selected_categories):
    temp_mods = []
    if len(selected_categories) > 0:
        for mod in mods:
            if mod.version.version == version:
                    mod_categories = [mod_category[1].name for mod_category in list(enumerate(mod.categories.all()))]
                    if all(map(lambda category: category in mod_categories, selected_categories)):
                        temp_mods.append(mod)
    else:
        for mod in mods:
            if mod.version.version == version:
                temp_mods.append(mod)
    return temp_mods

def home(request):
    mods = Mod.objects.all()
    if request.method == "POST":
        mods = filter_mods(mods, request.POST["version"], [selected_category[1] for selected_category in list(enumerate(request.POST))[2:]])

    data = {
        "categories": Category.objects.all(),
        "versions": sort_versions(Version.objects.all()),
        "mods": mods
    }

    return render(request, "main/html/home.html", data)
