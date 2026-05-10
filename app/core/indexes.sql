CREATE INDEX idx_users_xp
ON users(xp);

CREATE INDEX idx_questions_topic
ON questions(topic);

CREATE INDEX idx_questions_difficulty
ON questions(difficulty);

CREATE INDEX idx_test_sessions_user
ON test_sessions(user_id);

CREATE INDEX idx_notifications_user
ON notifications(user_id);