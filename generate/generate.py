import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_graphs(filename):
    # Read the data
    df = pd.read_csv(filename, sep=';')

    # Convert necessary columns to numeric types
    df['tick_nr'] = pd.to_numeric(df['tick_nr'])
    df['score'] = pd.to_numeric(df['score'])
    df['completeness'] = pd.to_numeric(df['completeness'])

    # Plot Score over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['tick_nr'], df['score'], marker='o', linestyle='-', label='Score')
    plt.xlabel('Tick Number')
    plt.ylabel('Score')
    plt.title('Score Progression Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('score_progression.png')  # Save the figure as an image
    plt.show()

    # Plot Completeness over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['tick_nr'], df['completeness'], marker='s', linestyle='-', color='r', label='Completeness')
    plt.xlabel('Tick Number')
    plt.ylabel('Completeness')
    plt.title('Completeness Progression Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('completeness_progression.png')  # Save the figure as an image
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
    else:
        plot_graphs(sys.argv[1])