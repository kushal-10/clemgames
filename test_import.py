import importlib


def import_method(method_path: str):
    """
    Import the method from the specified module path.
    
    Args:
        method_path (str): The method path separated by dots. Example - clemcore.backends.multimodal_utils.generate_internvl2_prompt_text

    Returns:
        type: The imported method.

    Raises:
        ImportError: If the method cannot be imported.
    """
    try:
        module_path, method_name = method_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, method_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not import method '{method_name}' from module '{module_path}'. Error: {e}") from e

# Test the import
method = import_method("backends.multimodal_utils.generate_internvl2_prompt_text")
print(method)