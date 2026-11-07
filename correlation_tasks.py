"""Задачи второй части лабораторной: корреляционный анализ."""
from __future__ import annotations

from grader_contracts.correlation_tasks import BrainCorrelationSummary, BrainDataInput

import pandas as pd

FEATURES = ["FSIQ", "VIQ", "PIQ", "Weight", "Height"]


def analyze_brain_correlations(data: BrainDataInput) -> BrainCorrelationSummary:
    df = pd.read_csv(data.csv_path, sep="\\t", na_values=["NA"])

    men = df.loc[df["Gender"] == "Male"]
    women = df.loc[df["Gender"] == "Female"]

    men_corr = men[FEATURES + ["MRI_Count"]].corr(method="pearson")["MRI_Count"]
    women_corr = women[FEATURES + ["MRI_Count"]].corr(method="pearson")["MRI_Count"]

    men_mri_correlation = {
        feature: float(men_corr[feature]) for feature in FEATURES
    }
    women_mri_correlation = {
        feature: float(women_corr[feature]) for feature in FEATURES
    }

    all_correlations = [
        (feature, value)
        for correlations in (men_mri_correlation, women_mri_correlation)
        for feature, value in correlations.items()
        if pd.notna(value)
    ]
    strongest_mri_feature = max(
        all_correlations, key=lambda item: abs(item[1])
    )[0] if all_correlations else ""

    return BrainCorrelationSummary(
        men_count=int(len(men)),
        women_count=int(len(women)),
        women_mri_correlation=women_mri_correlation,
        men_mri_correlation=men_mri_correlation,
        strongest_mri_feature=strongest_mri_feature,
    )
