import jwt, time, sys
KEY = "lab7-secret-key-1234567890-abcdef"
p = {"sub": "ann", "role": "user", "iss": "lab7", "aud": "students",
     "exp": int(time.time()) + 3600}
if len(sys.argv) > 1 and sys.argv[1] == "bad":
    p["role"] = "admin"
    print(jwt.encode(p, None, algorithm="none"))
else:
    print(jwt.encode(p, KEY, algorithm="HS256"))
