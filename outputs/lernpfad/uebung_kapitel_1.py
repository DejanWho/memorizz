"""Lernpfad memorizz — Übung zu Kapitel 1 (Orientierung).

Aufgabe: Gib für jeden ApplicationMode die aktiven Memory-Typen aus und nenne
am Ende die Typen, die in ALLEN drei Modi vorkommen (die „Grundausstattung“).

Ausführen aus dem Repo-Root:   python outputs/lernpfad/uebung_kapitel_1.py
Kein API-Key nötig — es werden nur die Enums aus src/memorizz/enums/ gelesen.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Das Paket liegt im src-Layout; ohne `pip install -e .` machen wir es so importierbar:
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from memorizz.enums import ApplicationMode  # noqa: E402
from memorizz.enums.application_mode import ApplicationModeConfig  # noqa: E402

# Nützlich: ApplicationModeConfig.get_memory_types(mode) -> list[MemoryType]
#           MemoryType-Mitglieder haben .name (z. B. "KNOWLEDGE_BASE") und .value ("knowledge_base")
# Achtung: ApplicationMode.DEFAULT ist nur ein Alias für ASSISTANT — beim Iterieren
#          über ApplicationMode taucht er deshalb NICHT als eigenes Mitglied auf.

modes = list(ApplicationMode)


def main() -> None:
    # TODO (5–8 Zeilen):
    #   1. Für jeden Modus in `modes` die Memory-Typen ausgeben, z. B.
    #        assistant: conversation_memory, knowledge_base, ...

    for mode in modes:
        memory_types = ApplicationModeConfig.get_memory_types(mode)
        memory_type_names = [mt.name for mt in memory_types]
        print(f"{mode.name.lower()}: {', '.join(memory_type_names)}")


    #   2. Die Schnittmenge aller Typen bilden (Tipp: set-Intersection über die
    #      Listen aus get_memory_types) und als "Grundausstattung: ..." ausgeben.
    #   Erwartung: drei Typen sind in allen Modi enthalten. Welche — und warum
    #   ergibt das Sinn? (Kurz im Chat beantworten.)
    # Schnittmenge aller Typen bilden
    all_memory_types = [set(ApplicationModeConfig.get_memory_types(mode)) for mode in modes]
    common_memory_types = set.intersection(*all_memory_types)
    common_memory_type_names = [mt.name for mt in common_memory_types]
    print(f"Grundausstattung: {', '.join(common_memory_type_names)}")


if __name__ == "__main__":
    main()
