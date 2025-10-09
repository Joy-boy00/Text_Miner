import sqlite3

# Connect (or create) the SQLite database
conn = sqlite3.connect("sentiment_analysis.db")
cursor = conn.cursor()

# Create Sentence_Database
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sentence_Database (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sentence TEXT NOT NULL,
    score INTEGER,
    sentiment TEXT CHECK(sentiment IN ('positive', 'negative'))
);
""")

# Create Word_List_Database
cursor.execute("""
CREATE TABLE IF NOT EXISTS Word_List_Database (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL UNIQUE,
    sentiment TEXT CHECK(sentiment IN ('positive', 'negative')),
    is_available_in_dict BOOLEAN DEFAULT 0
);
""")

# Create Analysis_Database
cursor.execute("""
CREATE TABLE IF NOT EXISTS Analysis_Database (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_sentences INTEGER DEFAULT 0,
    total_paras INTEGER DEFAULT 0,
    total_score INTEGER DEFAULT 0,
    total_words INTEGER DEFAULT 0,
    total_negative_words INTEGER DEFAULT 0,
    total_positive_words INTEGER DEFAULT 0,
    total_dict_hits INTEGER DEFAULT 0,
    total_dict_miss INTEGER DEFAULT 0,
    total_positive_sentences INTEGER DEFAULT 0,
    total_negative_sentences INTEGER DEFAULT 0
);
""")

# Commit and close connection
conn.commit()
conn.close()