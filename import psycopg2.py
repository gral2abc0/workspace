import psycopg2

db_config = {
    "host": "192.168.20.69",
    "port": "15432",
    "database": "security_db",
    "user": "admin",
    "password": "test1!"
}

def test_db_connection():
    try:
        # 1. conn 객체에 'with'를 사용하여 자동으로 close()되게 함
        with psycopg2.connect(**db_config) as conn:
            print("✅ 데이터베이스 연결 성공!")
            
            # 2. cur 객체에 'with'를 사용하여 커서도 자동으로 close()되게 함
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                db_version = cur.fetchone()
                print(f"📌 데이터베이스 버전: {db_version}")
                
        # with 블록을 빠져나오면 conn과 cur이 자동으로 닫힘
        print("🔒 리소스가 안전하게 정리되었습니다.")
        
    except Exception as e:
        print(f"❌ 데이터베이스 연결 실패: {e}")

if __name__ == "__main__":
    test_db_connection()