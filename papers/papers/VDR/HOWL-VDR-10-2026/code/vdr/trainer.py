# code/vdr/trainer.py
from __future__ import annotations

from typing import Dict, List, Sequence, Tuple

from .vdr import VDR
from .linalg import Vec
from .losses import mse, mse_grad
from .metrics import argmax_vec


def train_step(model, x: Vec, y: Vec, optimizer):
    optimizer.zero_grad()
    pred = model.forward(x)
    loss = mse(pred, y)
    grad = mse_grad(pred, y)
    model.backward(grad)
    optimizer.step()
    return loss, pred


def train_epoch(model, dataset, optimizer):
    total = VDR(0)
    preds = []
    for x, y in dataset:
        loss, pred = train_step(model, x, y, optimizer)
        total = total + loss
        preds.append(pred)
    return {
        "avg_loss": (total / VDR(len(dataset))).normalize(),
        "preds": preds,
    }


def evaluate_epoch(model, dataset):
    total = VDR(0)
    preds = []
    for x, y in dataset:
        pred = model.forward(x)
        loss = mse(pred, y)
        total = total + loss
        preds.append(pred)
    return {
        "avg_loss": (total / VDR(len(dataset))).normalize(),
        "preds": preds,
    }


def predict_class(model, x: Vec) -> int:
    y = model.forward(x)
    return argmax_vec(y)


def evaluate_classification(model, dataset):
    pred_ids = []
    target_ids = []
    for x, target_idx in dataset:
        pred_ids.append(predict_class(model, x))
        target_ids.append(target_idx)

    correct = 0
    for p, t in zip(pred_ids, target_ids):
        if p == t:
            correct += 1

    return {
        "pred_ids": pred_ids,
        "target_ids": target_ids,
        "accuracy": VDR(correct, len(dataset)).normalize(),
    }
