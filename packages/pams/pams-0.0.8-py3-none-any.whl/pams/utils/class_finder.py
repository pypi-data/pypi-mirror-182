from typing import List
from typing import Optional
from typing import Type


def find_class(name: str, optional_class_list: Optional[List[Type]] = None) -> Type:
    _1 = __import__("pams", globals(), locals())
    _2 = __import__("pams.agents", globals(), locals(), ["*"])
    _3 = __import__("pams.events", globals(), locals(), ["*"])

    candidates_spaces = [*globals().values(), *locals().values()]

    object_class_candidates = [
        getattr(m, name) for m in candidates_spaces if hasattr(m, name)
    ]
    if optional_class_list is not None:
        object_class_candidates.extend(
            [x for x in optional_class_list if x.__name__ == name]
        )
    if len(object_class_candidates) != 1:
        raise AttributeError(
            f"class for {name} is found {len(object_class_candidates)} times"
        )
    object_class: Type = object_class_candidates[0]
    return object_class
