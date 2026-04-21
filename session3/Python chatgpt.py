
# ==============================
# Configuration / Constants
# ==============================

def get_threshold():
    return 2.0

def get_feature_name():
    return "petal_length"

def get_positive_label():
    return "setosa"

def get_negative_label():
    return "not_setosa"

def get_label_key():
    return "species"


# ==============================
# Dataset Creation
# ==============================

def create_flower1():
    return {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

def create_flower2():
    return {
        "id": "flower2",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }

def create_dataset():
    flower1 = create_flower1()
    flower2 = create_flower2()
    return [flower1, flower2]


# ==============================
# Prediction / Classification
# ==============================

def predict_label(sample, feature_name, threshold, positive_label, negative_label):
    if sample[feature_name] < threshold:
        return positive_label
    else:
        return negative_label

def get_true_label(sample, label_key, positive_label, negative_label):
    if sample[label_key] == positive_label:
        return positive_label
    else:
        return negative_label


# ==============================
# Metrics Handling
# ==============================

def initialize_metrics():
    return 0, 0, 0, []

def update_metrics(y_pred, y_true, correct, wrong):
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1
    return correct, wrong

def update_total(total):
    return total + 1

def append_prediction(y_pred_list, y_pred):
    y_pred_list.append(y_pred)
    return y_pred_list


# ==============================
# Printing Functions
# ==============================

def print_start_message():
    print("\n=== Start session 3 Prediction Loop ===")

def print_sample_basic(sample):
    print(sample["id"], sample["petal_length"], sample["species"])

def print_sample_trace(sample, y_true, y_pred):
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample['petal_length']}"
    )

def print_summary(correct, wrong, total, accuracy, y_pred_list):
    print("\n=== session 3 Summary ===")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", y_pred_list)


# ==============================
# Accuracy Calculation
# ==============================

def calculate_accuracy(correct, total):
    if total > 0:
        return (correct / total) * 100
    else:
        return 0.0


# ==============================
# Main Execution
# ==============================

def main():
    # Get configuration
    threshold = get_threshold()
    feature_name = get_feature_name()
    positive_label = get_positive_label()
    negative_label = get_negative_label()
    label_key = get_label_key()

    # Initialize metrics
    correct, wrong, total, y_pred_list = initialize_metrics()

    # Create dataset
    dataset = create_dataset()

    # Start loop
    print_start_message()

    for sample in dataset:
        print_sample_basic(sample)

        # Prediction
        y_pred = predict_label(sample, feature_name, threshold, positive_label, negative_label)

        # True label
        y_true = get_true_label(sample, label_key, positive_label, negative_label)

        # Update metrics
        correct, wrong = update_metrics(y_pred, y_true, correct, wrong)
        total = update_total(total)
        y_pred_list = append_prediction(y_pred_list, y_pred)

        # Print trace
        print_sample_trace(sample, y_true, y_pred)

    # Final metrics
    accuracy = calculate_accuracy(correct, total)

    # Print summary
    print_summary(correct, wrong, total, accuracy, y_pred_list)


# Run the program
if __name__ == "__main__":
    main()
