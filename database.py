import sqlite3


def create_database():

    conn = sqlite3.connect(
        "resume_analysis.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analysis (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            ats_score INTEGER,

            match_score REAL,

            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conn.commit()
    conn.close()


def save_analysis(
    name,
    ats_score,
    match_score
):

    conn = sqlite3.connect(
        "resume_analysis.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis
        (
            name,
            ats_score,
            match_score
        )

        VALUES (?, ?, ?)
        """,
        (
            name,
            ats_score,
            match_score
        )
    )

    conn.commit()
    conn.close()


def get_all_analysis():

    conn = sqlite3.connect(
        "resume_analysis.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            name,
            ats_score,
            match_score,
            date
        FROM analysis
        ORDER BY id DESC
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data