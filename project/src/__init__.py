from pypendency.builder import container_builder
from pypendency.loaders.yaml_loader import YamlLoader

YamlLoader(container_builder).load_dir('/src/use_cases/_dependencies/')

