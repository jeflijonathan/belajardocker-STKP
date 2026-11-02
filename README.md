# STKP

docker ps -> Menampilkan semua kontainer yang sedang aktif

docker image ls -> Menampilkan daftar Docker Image yang tersimpan di dalam sistem lokal komputer Anda.

docker container ls -> Menampilkan daftar kontainer yang sedang aktif.

docker compose up -d

# cara melihat struktur dan file project

```sheel
tree /F
```

# struktur project

```folder
C:.
│   docker-compose.yaml
│   README.md
│
├───materi
│   └───STKP-2327240059
│       ├───P 2
│       │   │   docker-compose.yaml
│       │   │   README.md
│       │   │
│       │   └───nginx
│       │           index.html
│       │
│       ├───P 3
│       │       app.py
│       │       docker-compose.yaml
│       │       dockerfile
│       │       readme.md
│       │
│       ├───P4_paralel
│       │   │   docker-compose.yaml
│       │   │   Dockerfile
│       │   │
│       │   └───app
│       │           mimd-parallel.py
│       │           mimd.py
│       │           misd.py
│       │           simd.py
│       │           sisd.py
│       │
│       ├───P5_sequential_latihan
│       │       app-konkuren-multi-core.py
│       │       app-konkuren-single-core.py
│       │       app-parallel-speed-up.py
│       │       app-sequential.py
│       │       docker-compose.yaml
│       │       Dockerfile
│       │
│       ├───P8
│       │   │   docker-compose.yaml
│       │   │
│       │   └───python
│       │           multi-processing.py
│       │           multi-threading-multi-processing.py
│       │           multi-threading.py
│       │           process.py
│       │           thread.py
│       │
│       └───P9
│           │   docker-compose.yaml
│           │
│           └───python
│               │   mutex.py
│               │   race-condition.py
│               │   semaphore.py
│               │
│               └───P10
│                       deadlock.py
│                       livelock.py
│                       rpc_client.py
│                       rpc_server.py
│                       solusi_deadlock.py
│                       solusi_livelock.py
│
├───nginx
│       index.html
│
├───P 2
│   │   docker-compose.yaml
│   │   README.md
│   │
│   └───nginx
│           index.html
│
├───P 3
│       app.py
│       docker-compose.yaml
│       dockerfile
│       readme.md
│
├───p4
│   │   app.py
│   │   docker-compose.yaml
│   │   dockerfile
│   │   README.md
│   │
│   ├───multi
│   │       app.py
│   │       docker-compose.yaml
│   │       dockerfile
│   │
│   └───paraller
│       │   docker-compose.yaml
│       │   dockerfile
│       │   README.md
│       │
│       └───app
│               mimd-parallel.py
│               mimd.py
│               misd.py
│               simd.py
│               sisd.py
│
├───p5
│       docker-compose.yml
│       Dockerfile
│       paraller.py
│       perhitunganSekuensial.py
│       perhitungan_konkarensi.py
│       perhitungan_konkarensi_multi_core.py
│
├───P6
│       app.py
│       docker-compose.yml
│       Dockerfile
│
└───python
    ├───p10
    │       deadlock.py
    │       docker-compose.yaml
    │       livelock.py
    │       rpc_client.py
    │       rpc_server.py
    │       solusi_deadlock.py
    │       solusi_livelock.py
    │
    ├───p12
    │   │   application.py
    │   │   database.py
    │   │   docker-compose.yaml
    │   │   lamport.py
    │   │   presentation.py
    │   │
    │   ├───python
    │   ├───stkp_volume
    │   │   └───nginx
    │   └───__pycache__
    │           lamport.cpython-312.pyc
    │
    └───P9
            mutex.py
            race_condition.py
            semaphore.py

```
