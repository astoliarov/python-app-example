generate-grpc:
	python -m grpc_tools.protoc -I app/api/grpc --python_out=app/api/grpc --grpc_python_out=app/api/grpc app/api/grpc/interface.proto
