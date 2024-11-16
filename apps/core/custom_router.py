from django.urls import path
from django.views.generic import CreateView
from django.views.generic.detail import SingleObjectMixin

from django_router import Router
from django_router.settings import ROUTER_SETTINGS as settings
from django_router.utils import DJANGO_ADMIN_LIKE_MAP, DJANGO_ROUTER_MAP, from_camel


class CustomRouter(Router):
    def _push(self, func, pattern, view, name, kwargs):
        # Get second element of tuple.
        namespace = view.__module__.split(".")[1]  # <---

        self._namespaces.setdefault(namespace, []).append(
            (func, pattern, view, name, kwargs)
        )

    def _get_params(self, view, parameter_map):
        pattern_parts = []
        name_parts = []
        if settings.SIMPLE_AUTO_NAMING or not isinstance(view, type):
            _view = from_camel(view.__name__)  # <---

            # Replace suffix.
            suffix_replacements = {
                '_list': '',
                '_create': '/add',
                '_detail': '/<int:pk>',
                '_update': '/<int:pk>/update',
                '_delete': '/<int:pk>/delete'
            }

            for suffix, replacement in suffix_replacements.items():
                if _view.endswith(suffix):
                    _view = _view.replace(suffix, replacement)
                    break

            pattern_parts.append(_view)  # <---

            name_parts.append(from_camel(view.__name__))
        else:
            model = getattr(view, "model", None)
            model_name = ""
            object_name = model._meta.object_name if model else ""
            if model:
                if settings.MODEL_NAMES_MONOLITHIC:
                    model_name = model._meta.model_name
                else:
                    model_name = from_camel(model._meta.object_name)

                pattern_parts.append(model_name)
                name_parts.append(model_name)

            if issubclass(view, SingleObjectMixin) and not issubclass(view, CreateView):
                pattern_parts.append("<int:pk>")

            parameters = (
                from_camel(view.__name__.replace(object_name, "")),
                from_camel(view.__name__.replace(object_name, "")),
            )
            for key in parameter_map:
                if issubclass(view, key):
                    parameters = parameter_map[key]
                    break

            if parameters[1]:
                pattern_parts.append(parameters[1])

            name_parts.append(parameters[0].replace(model_name, ""))

        pattern = "/".join(pattern_parts) + "/"
        name = settings.WORDS_SEPARATOR.join(name_parts)

        return pattern, name

    @property
    def urlpatterns(self):
        if settings.ADMIN_LIKE_VERBS:
            parameter_map = DJANGO_ADMIN_LIKE_MAP
        else:
            parameter_map = DJANGO_ROUTER_MAP
        urlpatterns = []
        for namespace, patterns in self._namespaces.items():
            paths = []
            for func, pattern, view, name, kwargs in patterns:
                _pattern, _name = self._get_params(view, parameter_map)
                if not name:
                    name = _name
                if pattern is None:
                    pattern = _pattern
                if settings.MODULE_PATH_MAP:
                    path_map = view.__module__.split(".")[1:-1]
                else:
                    path_map = []
                pattern = "/".join(path_map + [pattern])

                # "slugify" url
                pattern = pattern.replace("_", "-")

                paths.append(
                    func(
                        pattern,
                        view.as_view() if isinstance(view, type) else view,
                        name=name,
                        kwargs=kwargs,
                    )
                )
            # urlpatterns.append(path(f"{namespace}/", (paths, namespace, namespace)))
            urlpatterns.append(path("", (paths, namespace, namespace)))  # <---

        return urlpatterns


router = CustomRouter()
