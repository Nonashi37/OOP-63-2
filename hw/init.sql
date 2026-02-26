-- Таблица команд (Родительская)
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    tech_stack TEXT
);

-- Таблица сервисов (Дочерняя)
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    status TEXT CHECK(status IN ('stable', 'down', 'legacy')),
    team_id INTEGER, -- Наш будущий мостик
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);



-- Добавляем команды
INSERT INTO teams (name, tech_stack) VALUES
('Backend Beasts', 'Python, FastAPI'),
('Frontend Fairies', 'React, TS'),
('DevOps Wizards', 'K8s, Terraform');

-- Добавляем сервисы и привязываем их к ID команд
INSERT INTO services (service_name, status, team_id) VALUES
('Auth-Service', 'stable', 1),
('Payment-Gateway', 'down', 1),
('Admin-Dashboard', 'stable', 2),
('Legacy-Crap', 'legacy', 3);


-- Соединяем
SELECT
    s.service_name,
    s.status,
    t.name AS responsible_team
FROM services s
JOIN teams t ON s.team_id = t.team_id;



-- Создаем Вюю
CREATE VIEW v_problem_services AS
SELECT
    s.service_name,
    t.name AS team_to_blame
FROM services s
JOIN teams t ON s.team_id = t.team_id
WHERE s.status = 'down';

-- Теперь юзать это можно как обычную таблицу:
SELECT * FROM v_problem_services;

SELECT s.service_name, t.name
FROM services s
JOIN teams t ON s.team_id = t.team_id;


INSERT INTO services (service_name, status, team_id)
VALUES ('Ghost-Service', 'stable', 999);