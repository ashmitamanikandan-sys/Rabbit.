/**
 * RABBIT Unified Views Coordinator
 * Manages the active view container (#app), cleanly transitioning between:
 * - Home (Curiosity Feed & Reader)
 * - Warren (Community Discussions & Stories)
 * - Clubs (Reading Groups & Chats)
 * - Profile (Signature "Your Little Universe" & Saved Library)
 * - Auth (Redesigned "Your rabbit hole awaits")
 */
(function() {
  "use strict";

  let mainContainer = null;

  function getContainer() {
    if (!mainContainer) {
      mainContainer = document.getElementById("app");
    }
    return mainContainer;
  }

  window.RabbitUnifiedViews = {
    showHome: function() {
      const app = getContainer();
      if (!app) return;
      document.body.dataset.rabbitStage = "curiosity";
      if (typeof renderHome === "function") {
        renderHome();
      }
      if (window.RabbitNavigation) {
        window.RabbitNavigation.setActiveTab("home");
      }
    },

    showWarren: function() {
      const app = getContainer();
      if (!app) return;
      document.body.dataset.rabbitStage = "warren";
      if (window.RabbitCommunityViews) {
        window.RabbitCommunityViews.renderWarren(app);
      }
      if (window.RabbitNavigation) {
        window.RabbitNavigation.setActiveTab("warren");
      }
    },

    showClubs: function() {
      const app = getContainer();
      if (!app) return;
      document.body.dataset.rabbitStage = "clubs";
      if (window.RabbitCommunityViews) {
        window.RabbitCommunityViews.renderClubs(app);
      }
      if (window.RabbitNavigation) {
        window.RabbitNavigation.setActiveTab("clubs");
      }
    },

    showProfile: function() {
      const app = getContainer();
      if (!app) return;
      document.body.dataset.rabbitStage = "profile";
      if (window.RabbitProfile) {
        window.RabbitProfile.render(app);
      }
      if (window.RabbitNavigation) {
        window.RabbitNavigation.setActiveTab("profile");
      }
    },

    showAuth: function(isSignUp) {
      const app = getContainer();
      if (!app) return;
      document.body.dataset.rabbitStage = "auth";
      if (window.RabbitAuth) {
        window.RabbitAuth.render(app, isSignUp);
      }
    }
  };
})();
