# Real-Time Object Detection & Logging Platform

A beginner-friendly real-time object detection project using YOLO, OpenCV, Python, MacBook webcam, and MySQL.

## 1. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install packages

```bash
pip install -r requirements.txt
```

## 3. Install and start MySQL

If MySQL is not installed:

```bash
brew install mysql
brew services start mysql
```

Set a MySQL password if required:

```bash
mysql_secure_installation
```

## 4. Create database

Run:

```bash
mysql -u root -p < database_schema.sql
```

Then edit `.env` and put your MySQL password:

```text
DB_PASSWORD=YOUR_MYSQL_PASSWORD
```

## 5. Run the project

```bash
python3 main.py
```

The first run downloads the YOLO model automatically.

Press `Q` in the detection window to stop.

## macOS camera permission

If the webcam does not open, go to:

System Settings → Privacy & Security → Camera

Allow camera access for the application running Python/VS Code/Terminal, then restart it.

## Project flow

Webcam → OpenCV → YOLO → Detection → UI → MySQL

## Notes

The database logging is optional. If MySQL is unavailable, the webcam detector still runs and displays detections.
