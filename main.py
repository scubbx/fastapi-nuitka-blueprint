#!python3

import sys, os

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Empty Description')
    parser.add_argument('-i', '--info', required=False, default="empty", help='an empty argument')
    parser.add_argument('-p', '--port', required=False, type=int, default=8181, help='port of the service')
    args = parser.parse_args()

    os.environ['NMS_info'] = args.info
    os.environ['NMS_port'] = str(args.port)

    import uvicorn
    print(f"program call was: {sys.argv}")
    uvicorn.run("service.demoservice:app", host="0.0.0.0", port=int(os.environ['NMS_port']), workers=2)