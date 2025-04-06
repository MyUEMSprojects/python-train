# a. Single Responsibility (Com funções pequenas):
# Não pythonico
def process_data(data):
    # Valida, limpa, transforma e salva
    ...


# Pythonico
def validate_data(data): ...
def clean_data(data): ...
def transform_data(data): ...
def save_data(data): ...


# b. Open/Closed (Usando ABCs):
from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, data): ...


class CSVExporter(Exporter):
    def export(self, data): ...


class JSONExporter(Exporter):
    def export(self, data): ...
