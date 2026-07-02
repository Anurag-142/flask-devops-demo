import os

from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-secret-key"),
        APP_NAME="Flask DevOps Demo",
        APP_DESCRIPTION="A polished, production-minded Flask application for demos and CI/CD pipelines.",
    )

    @app.get("/")
    def home():
        return render_template(
            "index.html",
            app_name=app.config["APP_NAME"],
            app_description=app.config["APP_DESCRIPTION"],
        )

    @app.get("/health")
    def health():
        return {
            "status": "ok",
            "service": app.config["APP_NAME"],
        }, 200

    @app.errorhandler(404)
    def not_found(_error):
        return render_template(
            "index.html",
            app_name=app.config["APP_NAME"],
            app_description=app.config["APP_DESCRIPTION"],
            error=True,
        ), 404

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG", "0").lower() in {"1", "true", "yes"},
    )
