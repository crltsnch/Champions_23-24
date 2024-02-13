from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import csv

#Obtener tabla de partidos de octavos del contenido de wikipedia

html = """<!DOCTYPE html>
<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available" lang="es" dir="ltr">
<head>
<meta charset="UTF-8">
<title>Anexo:Octavos de final de la Liga de Campeones de la UEFA 2022-23 - Wikipedia, la enciclopedia libre</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-sticky-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-0 vector-feature-client-preferences-disabled vector-feature-client-prefs-pinned-disabled vector-feature-night-mode-disabled skin-night-mode-clientpref-0 vector-toc-available";var cookie=document.cookie.match(/(?:^|; )eswikimwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":[",\t."," \t,"],
"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],"wgRequestId":"e053f9bb-108f-460f-a79a-cae648416756","wgCanonicalNamespace":"Anexo","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":104,"wgPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23","wgTitle":"Octavos de final de la Liga de Campeones de la UEFA 2022-23","wgCurRevisionId":157852274,"wgRevisionId":157852274,"wgArticleId":10376179,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Liga de Campeones de la UEFA 2022-23"],"wgPageViewLanguage":"es","wgPageContentLanguage":"es","wgPageContentModel":"wikitext","wgRelevantPageName":"Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23","wgRelevantArticleId":10376179,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,
"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoticeProject":"wikipedia","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsFlags":6,"wgVisualEditor":{"pageLanguageCode":"es","pageLanguageDir":"ltr","pageVariantFallbacks":"es"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":true,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":40000,"wgULSCurrentAutonym":"español","wgCentralAuthMobileDomain":false,"wgEditSubmitButtonLabelPublish":true,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,"wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgCheckUserClientHintsHeadersJsApi":["architecture","bitness","brands","fullVersionList","mobile","model","platform","platformVersion"],"GEHomepageSuggestedEditsEnableTopics":true,"wgGETopicsMatchModeEnabled":true,"wgGEStructuredTaskRejectionReasonTextInputEnabled":false,"wgGELevelingUpEnabledForUser":false};RLSTATE={
"skins.vector.user.styles":"ready","ext.gadget.imagenesinfobox":"ready","ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","skins.vector.user":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.cite.styles":"ready","codex-search-styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","wikibase.client.init":"ready","ext.wikimediaBadges":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","mediawiki.toggleAllCollapsibles","site","mediawiki.page.ready","mediawiki.toc","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.a-commons-directo","ext.gadget.ReferenceTooltips","ext.gadget.refToolbar","ext.gadget.switcher","ext.urlShortener.toolbar","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init",
"ext.visualEditor.targetLoader","ext.echo.centralauth","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.cx.uls.quick.actions","ext.checkUser.clientHints"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
}];});});</script>
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=codex-search-styles%7Cext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cskins.vector.icons%2Cstyles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector-2022">
<script async="" src="/w/load.php?lang=es&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector-2022"></script>
<meta name="ResourceLoaderDynamicStyles" content="">
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=ext.gadget.imagenesinfobox&amp;only=styles&amp;skin=vector-2022">
<link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=site.styles&amp;only=styles&amp;skin=vector-2022">
<noscript><link rel="stylesheet" href="/w/load.php?lang=es&amp;modules=noscript&amp;only=styles&amp;skin=vector-2022"></noscript>
<meta name="generator" content="MediaWiki 1.42.0-wmf.17">
<meta name="referrer" content="origin">
<meta name="referrer" content="origin-when-cross-origin">
<meta name="robots" content="max-image-preview:standard">
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=1000">
<meta property="og:title" content="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2022-23 - Wikipedia, la enciclopedia libre">
<meta property="og:type" content="website">
<link rel="preconnect" href="//upload.wikimedia.org">
<link rel="alternate" media="only screen and (max-width: 720px)" href="//es.m.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23">
<link rel="alternate" type="application/x-wiki" title="Editar" href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">
<link rel="icon" href="/static/favicon/wikipedia.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (es)">
<link rel="EditURI" type="application/rsd+xml" href="//es.wikipedia.org/w/api.php?action=rsd">
<link rel="canonical" href="https://es.wikipedia.org/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">
<link rel="alternate" type="application/atom+xml" title="Canal Atom de Wikipedia" href="/w/index.php?title=Especial:CambiosRecientes&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="//login.wikimedia.org">
</head>
<body class="skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-104 ns-subject mw-editable page-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23 rootpage-Anexo_Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23 skin-vector-2022 action-view"><a class="mw-jump-link" href="#bodyContent">Ir al contenido</a>
<div class="vector-header-container">
	<header class="vector-header mw-header">
		<div class="vector-header-start">
			<nav class="vector-main-menu-landmark" aria-label="Sitio" role="navigation">
				
<div id="vector-main-menu-dropdown" class="vector-dropdown vector-main-menu-dropdown vector-button-flush-left vector-button-flush-right"  >
	<input type="checkbox" id="vector-main-menu-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-main-menu-dropdown" class="vector-dropdown-checkbox "  aria-label="Menú principal"  >
	<label id="vector-main-menu-dropdown-label" for="vector-main-menu-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-menu mw-ui-icon-wikimedia-menu"></span>

<span class="vector-dropdown-label-text">Menú principal</span>
	</label>
	<div class="vector-dropdown-content">


				<div id="vector-main-menu-unpinned-container" class="vector-unpinned-container">
		
<div id="vector-main-menu" class="vector-main-menu vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-main-menu-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="main-menu-pinned"
	data-pinnable-element-id="vector-main-menu"
	data-pinned-container-id="vector-main-menu-pinned-container"
	data-unpinned-container-id="vector-main-menu-unpinned-container"
>
	<div class="vector-pinnable-header-label">Menú principal</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-main-menu.pin">mover a la barra lateral</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-main-menu.unpin">ocultar</button>
</div>

	
<div id="p-navigation" class="vector-menu mw-portlet mw-portlet-navigation"  >
	<div class="vector-menu-heading">
		Navegación
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="n-mainpage-description" class="mw-list-item"><a href="/wiki/Wikipedia:Portada" title="Visitar la página principal [z]" accesskey="z"><span>Portada</span></a></li><li id="n-portal" class="mw-list-item"><a href="/wiki/Portal:Comunidad" title="Acerca del proyecto, lo que puedes hacer, dónde encontrar información"><span>Portal de la comunidad</span></a></li><li id="n-currentevents" class="mw-list-item"><a href="/wiki/Portal:Actualidad" title="Encuentra información de contexto sobre acontecimientos actuales"><span>Actualidad</span></a></li><li id="n-recentchanges" class="mw-list-item"><a href="/wiki/Especial:CambiosRecientes" title="Lista de cambios recientes en la wiki [r]" accesskey="r"><span>Cambios recientes</span></a></li><li id="n-newpages" class="mw-list-item"><a href="/wiki/Especial:P%C3%A1ginasNuevas"><span>Páginas nuevas</span></a></li><li id="n-randompage" class="mw-list-item"><a href="/wiki/Especial:Aleatoria" title="Cargar una página al azar [x]" accesskey="x"><span>Página aleatoria</span></a></li><li id="n-help" class="mw-list-item"><a href="/wiki/Ayuda:Contenidos" title="El lugar para aprender"><span>Ayuda</span></a></li><li id="n-sitesupport" class="mw-list-item"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_es.wikipedia.org&amp;uselang=es" title="Apóyanos"><span>Donaciones</span></a></li><li id="n-bug_in_article" class="mw-list-item"><a href="/wiki/Wikipedia:Informes_de_error"><span>Notificar un error</span></a></li>
		</ul>
		
	</div>
</div>

	
	
	
<div class="vector-main-menu-action vector-main-menu-action-lang-alert vector-main-menu-action-lang-alert-empty">
	<div class="vector-main-menu-action-item">
		<div class="vector-main-menu-action-heading vector-menu-heading">Idiomas</div>
		<div class="vector-main-menu-action-content vector-menu-content">
			<div class="mw-message-box cdx-message cdx-message--block mw-message-box-notice cdx-message--notice vector-language-sidebar-alert"><span class="cdx-message__icon"></span><div class="cdx-message__content">Los enlaces de idiomas se encuentran en la parte superior de la página, frente al título.</div></div>
		</div>
	</div>
</div>

</div>

				</div>

	</div>
</div>

		</nav>
			
<a href="/wiki/Wikipedia:Portada" class="mw-logo">
	<img class="mw-logo-icon" src="/static/images/icons/wikipedia.png" alt="" aria-hidden="true" height="50" width="50">
	<span class="mw-logo-container">
		<img class="mw-logo-wordmark" alt="Wikipedia" src="/static/images/mobile/copyright/wikipedia-wordmark-en.svg" style="width: 7.5em; height: 1.125em;">
		<img class="mw-logo-tagline" alt="La enciclopedia libre" src="/static/images/mobile/copyright/wikipedia-tagline-es.svg" width="120" height="13" style="width: 7.5em; height: 0.8125em;">
	</span>
</a>

		</div>
		<div class="vector-header-end">
			
<div id="p-search" role="search" class="vector-search-box-vue  vector-search-box-collapses vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box">
	<a href="/wiki/Especial:Buscar" class="cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only search-toggle" id="" title="Buscar en este wiki [f]" accesskey="f"><span class="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search"></span>

<span>Buscar</span>
	</a>
	<div class="vector-typeahead-search-container">
		<div class="cdx-typeahead-search cdx-typeahead-search--show-thumbnail cdx-typeahead-search--auto-expand-width">
			<form action="/w/index.php" id="searchform" class="cdx-search-input cdx-search-input--has-end-button">
				<div id="simpleSearch" class="cdx-search-input__input-wrapper"  data-search-loc="header-moved">
					<div class="cdx-text-input cdx-text-input--has-start-icon">
						<input
							class="cdx-text-input__input"
							 type="search" name="search" placeholder="Buscar en Wikipedia" aria-label="Buscar en Wikipedia" autocapitalize="sentences" title="Buscar en este wiki [f]" accesskey="f" id="searchInput"
							>
						<span class="cdx-text-input__icon cdx-text-input__start-icon"></span>
					</div>
					<input type="hidden" name="title" value="Especial:Buscar">
				</div>
				<button class="cdx-button cdx-search-input__end-button">Buscar</button>
			</form>
		</div>
	</div>
</div>

			<nav class="vector-user-links vector-user-links-wide" aria-label="Herramientas personales" role="navigation" >
	<div class="vector-user-links-main">
	
<div id="p-vector-user-menu-preferences" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	
<div id="p-vector-user-menu-userpage" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	<nav class="vector-client-prefs-landmark" aria-label="Tema">
		
		
	</nav>
	
<div id="p-vector-user-menu-notifications" class="vector-menu mw-portlet emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

	
<div id="p-vector-user-menu-overflow" class="vector-menu mw-portlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			<li id="pt-createaccount-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio" class=""><span>Crear una cuenta</span></a>
</li>
<li id="pt-login-2" class="user-links-collapsible-item mw-list-item user-links-collapsible-item"><a data-mw="interface" href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o" class=""><span>Acceder</span></a>
</li>

			
		</ul>
		
	</div>
</div>

	</div>
	
<div id="vector-user-links-dropdown" class="vector-dropdown vector-user-menu vector-button-flush-right vector-user-menu-logged-out"  title="Más opciones" >
	<input type="checkbox" id="vector-user-links-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-user-links-dropdown" class="vector-dropdown-checkbox "  aria-label="Herramientas personales"  >
	<label id="vector-user-links-dropdown-label" for="vector-user-links-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-ellipsis mw-ui-icon-wikimedia-ellipsis"></span>

<span class="vector-dropdown-label-text">Herramientas personales</span>
	</label>
	<div class="vector-dropdown-content">


		
<div id="p-personal" class="vector-menu mw-portlet mw-portlet-personal user-links-collapsible-item"  title="Menú de usuario" >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="pt-createaccount" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Crear_una_cuenta&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23" title="Te recomendamos crear una cuenta e iniciar sesión; sin embargo, no es obligatorio"><span class="vector-icon mw-ui-icon-userAdd mw-ui-icon-wikimedia-userAdd"></span> <span>Crear una cuenta</span></a></li><li id="pt-login" class="user-links-collapsible-item mw-list-item"><a href="/w/index.php?title=Especial:Entrar&amp;returnto=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23" title="Te recomendamos iniciar sesión, aunque no es obligatorio [o]" accesskey="o"><span class="vector-icon mw-ui-icon-logIn mw-ui-icon-wikimedia-logIn"></span> <span>Acceder</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-user-menu-anon-editor" class="vector-menu mw-portlet mw-portlet-user-menu-anon-editor"  >
	<div class="vector-menu-heading">
		Páginas para editores desconectados <a href="/wiki/Ayuda:Introducci%C3%B3n" aria-label="Obtenga más información sobre editar"><span>más información</span></a>
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="pt-anoncontribs" class="mw-list-item"><a href="/wiki/Especial:MisContribuciones" title="Una lista de modificaciones hechas desde esta dirección IP [y]" accesskey="y"><span>Contribuciones</span></a></li><li id="pt-anontalk" class="mw-list-item"><a href="/wiki/Especial:MiDiscusi%C3%B3n" title="Discusión sobre ediciones hechas desde esta dirección IP [n]" accesskey="n"><span>Discusión</span></a></li>
		</ul>
		
	</div>
</div>

	
	</div>
</div>

</nav>

		</div>
	</header>
</div>
<div class="mw-page-container">
	<div class="mw-page-container-inner">
		<div class="vector-sitenotice-container">
			<div id="siteNotice"><!-- CentralNotice --></div>
		</div>
		<div class="vector-column-start">
			<div class="vector-main-menu-container">
		<div id="mw-navigation">
			<nav id="mw-panel" class="vector-main-menu-landmark" aria-label="Sitio" role="navigation">
				<div id="vector-main-menu-pinned-container" class="vector-pinned-container">
				
				</div>
		</nav>
		</div>
	</div>
	<div class="vector-sticky-pinned-container">
				<nav id="mw-panel-toc" role="navigation" aria-label="Contenidos" data-event-name="ui.sidebar-toc" class="mw-table-of-contents-container vector-toc-landmark">
					<div id="vector-toc-pinned-container" class="vector-pinned-container">
					<div id="vector-toc" class="vector-toc vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-toc-pinnable-header vector-pinnable-header-pinned"
	data-feature-name="toc-pinned"
	data-pinnable-element-id="vector-toc"
	
	
>
	<h2 class="vector-pinnable-header-label">Contenidos</h2>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-toc.pin">mover a la barra lateral</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-toc.unpin">ocultar</button>
</div>


	<ul class="vector-toc-contents" id="mw-panel-toc-list">
		<li id="toc-mw-content-text"
			class="vector-toc-list-item vector-toc-level-1">
			<a href="#" class="vector-toc-link">
				<div class="vector-toc-text">Inicio</div>
			</a>
		</li>
		<li id="toc-Cuadro_de_clasificación"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Cuadro_de_clasificación">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">1</span>Cuadro de clasificación</div>
		</a>
		
		<ul id="toc-Cuadro_de_clasificación-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Participantes"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Participantes">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">2</span>Participantes</div>
		</a>
		
		<ul id="toc-Participantes-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Estadios"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Estadios">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">3</span>Estadios</div>
		</a>
		
		<ul id="toc-Estadios-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Llaves"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Llaves">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">4</span>Llaves</div>
		</a>
		
		<ul id="toc-Llaves-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Enfrentamientos"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Enfrentamientos">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">5</span>Enfrentamientos</div>
		</a>
		
			<button aria-controls="toc-Enfrentamientos-sublist" class="cdx-button cdx-button--weight-quiet cdx-button--icon-only vector-toc-toggle">
				<span class="vector-icon vector-icon--x-small mw-ui-icon-wikimedia-expand"></span>
				<span>Alternar subsección Enfrentamientos</span>
			</button>
		
		<ul id="toc-Enfrentamientos-sublist" class="vector-toc-list">
			<li id="toc-Leipzig_–_Manchester_City"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Leipzig_–_Manchester_City">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.1</span>Leipzig – Manchester City</div>
			</a>
			
			<ul id="toc-Leipzig_–_Manchester_City-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Brujas_–_Benfica"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Brujas_–_Benfica">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.2</span>Brujas – Benfica</div>
			</a>
			
			<ul id="toc-Brujas_–_Benfica-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Liverpool_–_Real_Madrid"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Liverpool_–_Real_Madrid">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.3</span>Liverpool – Real Madrid</div>
			</a>
			
			<ul id="toc-Liverpool_–_Real_Madrid-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Milan_–_Tottenham_Hotspur"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Milan_–_Tottenham_Hotspur">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.4</span>Milan – Tottenham Hotspur</div>
			</a>
			
			<ul id="toc-Milan_–_Tottenham_Hotspur-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Eintracht_Fráncfort_–_Napoli"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Eintracht_Fráncfort_–_Napoli">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.5</span>Eintracht Fráncfort – Napoli</div>
			</a>
			
			<ul id="toc-Eintracht_Fráncfort_–_Napoli-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Borussia_Dortmund_–_Chelsea"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Borussia_Dortmund_–_Chelsea">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.6</span>Borussia Dortmund – Chelsea</div>
			</a>
			
			<ul id="toc-Borussia_Dortmund_–_Chelsea-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Inter_de_Milán_–_Porto"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Inter_de_Milán_–_Porto">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.7</span>Inter de Milán – Porto</div>
			</a>
			
			<ul id="toc-Inter_de_Milán_–_Porto-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-París_Saint-Germain_–_Bayern_Múnich"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#París_Saint-Germain_–_Bayern_Múnich">
				<div class="vector-toc-text">
				<span class="vector-toc-numb">5.8</span>París Saint-Germain – Bayern Múnich</div>
			</a>
			
			<ul id="toc-París_Saint-Germain_–_Bayern_Múnich-sublist" class="vector-toc-list">
			</ul>
		</li>
	</ul>
	</li>
	<li id="toc-Clasificados_para_Cuartos_de_final"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Clasificados_para_Cuartos_de_final">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">6</span>Clasificados para Cuartos de final</div>
		</a>
		
		<ul id="toc-Clasificados_para_Cuartos_de_final-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Véase_también"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Véase_también">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">7</span>Véase también</div>
		</a>
		
		<ul id="toc-Véase_también-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Referencias"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Referencias">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">8</span>Referencias</div>
		</a>
		
		<ul id="toc-Referencias-sublist" class="vector-toc-list">
		</ul>
	</li>
	<li id="toc-Enlaces_externos"
		class="vector-toc-list-item vector-toc-level-1 vector-toc-list-item-expanded">
		<a class="vector-toc-link" href="#Enlaces_externos">
			<div class="vector-toc-text">
			<span class="vector-toc-numb">9</span>Enlaces externos</div>
		</a>
		
		<ul id="toc-Enlaces_externos-sublist" class="vector-toc-list">
		</ul>
	</li>
</ul>
</div>

					</div>
		</nav>
			</div>
		</div>
		<div class="mw-content-container">
			<main id="content" class="mw-body" role="main">
				<header class="mw-body-header vector-page-titlebar">
					<nav role="navigation" aria-label="Contenidos" class="vector-toc-landmark">
						
<div id="vector-page-titlebar-toc" class="vector-dropdown vector-page-titlebar-toc vector-button-flush-left"  >
	<input type="checkbox" id="vector-page-titlebar-toc-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-page-titlebar-toc" class="vector-dropdown-checkbox "  aria-label="Cambiar a la tabla de contenidos"  >
	<label id="vector-page-titlebar-toc-label" for="vector-page-titlebar-toc-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-listBullet mw-ui-icon-wikimedia-listBullet"></span>

<span class="vector-dropdown-label-text">Cambiar a la tabla de contenidos</span>
	</label>
	<div class="vector-dropdown-content">


							<div id="vector-page-titlebar-toc-unpinned-container" class="vector-unpinned-container">
			</div>
		
	</div>
</div>

					</nav>
					<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-namespace">Anexo</span><span class="mw-page-title-separator">:</span><span class="mw-page-title-main">Octavos de final de la Liga de Campeones de la UEFA 2022-23</span></h1>
							
<div id="p-lang-btn" class="vector-dropdown mw-portlet mw-portlet-lang"  >
	<input type="checkbox" id="p-lang-btn-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-lang-btn" class="vector-dropdown-checkbox mw-interlanguage-selector" aria-label="Este artículo existe sólo en este idioma. Añade el artículo para otros idiomas"   >
	<label id="p-lang-btn-label" for="p-lang-btn-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--action-progressive mw-portlet-lang-heading-0" aria-hidden="true"  ><span class="vector-icon mw-ui-icon-language-progressive mw-ui-icon-wikimedia-language-progressive"></span>

<span class="vector-dropdown-label-text">Añadir idiomas</span>
	</label>
	<div class="vector-dropdown-content">

		<div class="vector-menu-content">
			
			<ul class="vector-menu-content-list">
				
				
			</ul>
			<div class="after-portlet after-portlet-lang"><span class="uls-after-portlet-link"></span><span class="wb-langlinks-add wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:NewItem?site=eswiki&amp;page=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23" title="Agregar enlaces interlingüísticos" class="wbc-editpage">Añadir enlaces</a></span></div>
		</div>

	</div>
</div>
</header>
				<div class="vector-page-toolbar">
					<div class="vector-page-toolbar-container">
						<div id="left-navigation">
							<nav aria-label="Espacios de nombres">
								
<div id="p-associated-pages" class="vector-menu vector-menu-tabs mw-portlet mw-portlet-associated-pages"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-nstab-anexo" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Ver la página de contenido [c]" accesskey="c"><span>Anexo</span></a></li><li id="ca-talk" class="new vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo_discusi%C3%B3n:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;redlink=1" rel="discussion" title="Discusión acerca de la página (aún no redactado) [t]" accesskey="t"><span>Discusión</span></a></li>
		</ul>
		
	</div>
</div>

								
<div id="p-variants" class="vector-dropdown emptyPortlet"  >
	<input type="checkbox" id="p-variants-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-p-variants" class="vector-dropdown-checkbox " aria-label="Cambiar variante de idioma"   >
	<label id="p-variants-label" for="p-variants-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" aria-hidden="true"  ><span class="vector-dropdown-label-text">español</span>
	</label>
	<div class="vector-dropdown-content">


					
<div id="p-variants" class="vector-menu mw-portlet mw-portlet-variants emptyPortlet"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			
		</ul>
		
	</div>
</div>

				
	</div>
</div>

							</nav>
						</div>
						<div id="right-navigation" class="vector-collapsible">
							<nav aria-label="Vistas">
								
<div id="p-views" class="vector-menu vector-menu-tabs mw-portlet mw-portlet-views"  >
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-view" class="selected vector-tab-noicon mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23"><span>Leer</span></a></li><li id="ca-edit" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-history" class="vector-tab-noicon mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=history" title="Versiones anteriores de esta página [h]" accesskey="h"><span>Ver historial</span></a></li>
		</ul>
		
	</div>
</div>

							</nav>
				
							<nav class="vector-page-tools-landmark" aria-label="Página de herramientas">
								
<div id="vector-page-tools-dropdown" class="vector-dropdown vector-page-tools-dropdown"  >
	<input type="checkbox" id="vector-page-tools-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-page-tools-dropdown" class="vector-dropdown-checkbox "  aria-label="Herramientas"  >
	<label id="vector-page-tools-dropdown-label" for="vector-page-tools-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet" aria-hidden="true"  ><span class="vector-dropdown-label-text">Herramientas</span>
	</label>
	<div class="vector-dropdown-content">


									<div id="vector-page-tools-unpinned-container" class="vector-unpinned-container">
						
<div id="vector-page-tools" class="vector-page-tools vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-page-tools-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="page-tools-pinned"
	data-pinnable-element-id="vector-page-tools"
	data-pinned-container-id="vector-page-tools-pinned-container"
	data-unpinned-container-id="vector-page-tools-unpinned-container"
>
	<div class="vector-pinnable-header-label">Herramientas</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-page-tools.pin">mover a la barra lateral</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-page-tools.unpin">ocultar</button>
</div>

	
<div id="p-cactions" class="vector-menu mw-portlet mw-portlet-cactions emptyPortlet vector-has-collapsible-items"  title="Más opciones" >
	<div class="vector-menu-heading">
		Acciones
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="ca-more-view" class="selected vector-more-collapsible-item mw-list-item"><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23"><span>Leer</span></a></li><li id="ca-more-edit" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit" title="Editar esta página [e]" accesskey="e"><span>Editar</span></a></li><li id="ca-more-history" class="vector-more-collapsible-item mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=history"><span>Ver historial</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-tb" class="vector-menu mw-portlet mw-portlet-tb"  >
	<div class="vector-menu-heading">
		General
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="t-whatlinkshere" class="mw-list-item"><a href="/wiki/Especial:LoQueEnlazaAqu%C3%AD/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Lista de todas las páginas de la wiki que enlazan aquí [j]" accesskey="j"><span>Lo que enlaza aquí</span></a></li><li id="t-recentchangeslinked" class="mw-list-item"><a href="/wiki/Especial:CambiosEnEnlazadas/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" rel="nofollow" title="Cambios recientes en las páginas que enlazan con esta [k]" accesskey="k"><span>Cambios en enlazadas</span></a></li><li id="t-upload" class="mw-list-item"><a href="//commons.wikimedia.org/wiki/Special:UploadWizard?uselang=es" title="Subir archivos [u]" accesskey="u"><span>Subir archivo</span></a></li><li id="t-specialpages" class="mw-list-item"><a href="/wiki/Especial:P%C3%A1ginasEspeciales" title="Lista de todas las páginas especiales [q]" accesskey="q"><span>Páginas especiales</span></a></li><li id="t-permalink" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;oldid=157852274" title="Enlace permanente a esta versión de la página"><span>Enlace permanente</span></a></li><li id="t-info" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=info" title="Más información sobre esta página"><span>Información de la página</span></a></li><li id="t-cite" class="mw-list-item"><a href="/w/index.php?title=Especial:Citar&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;id=157852274&amp;wpFormIdentifier=titleform" title="Información sobre cómo citar esta página"><span>Citar esta página</span></a></li><li id="t-urlshortener" class="mw-list-item"><a href="/w/index.php?title=Especial:Acortador_de_URL&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23"><span>Obtener URL acortado</span></a></li><li id="t-urlshortener-qrcode" class="mw-list-item"><a href="/w/index.php?title=Especial:QrCode&amp;url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FAnexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23"><span>Download QR code</span></a></li>
		</ul>
		
	</div>
</div>

<div id="p-coll-print_export" class="vector-menu mw-portlet mw-portlet-coll-print_export"  >
	<div class="vector-menu-heading">
		Imprimir/exportar
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="coll-create_a_book" class="mw-list-item"><a href="/w/index.php?title=Especial:Libro&amp;bookcmd=book_creator&amp;referer=Anexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23"><span>Crear un libro</span></a></li><li id="coll-download-as-rl" class="mw-list-item"><a href="/w/index.php?title=Especial:DownloadAsPdf&amp;page=Anexo%3AOctavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=show-download-screen"><span>Descargar como PDF</span></a></li><li id="t-print" class="mw-list-item"><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;printable=yes" title="Versión imprimible de esta página [p]" accesskey="p"><span>Versión para imprimir</span></a></li>
		</ul>
		
	</div>
</div>

</div>

									</div>
				
	</div>
</div>

							</nav>
						</div>
					</div>
				</div>
				<div class="vector-column-end">
					<div class="vector-sticky-pinned-container">
						<nav class="vector-page-tools-landmark" aria-label="Página de herramientas">
							<div id="vector-page-tools-pinned-container" class="vector-pinned-container">
				
							</div>
		</nav>
						<nav class="vector-client-prefs-landmark" aria-label="Tema">
						</nav>
					</div>
				</div>
				<div id="bodyContent" class="vector-body" aria-labelledby="firstHeading" data-mw-ve-target-container>
					<div class="vector-body-before-content">
							<div class="mw-indicators">
		</div>

						<div id="siteSub" class="noprint">De Wikipedia, la enciclopedia libre</div>
					</div>
					<div id="contentSub"><div id="mw-content-subtitle"></div></div>
					
					
					<div id="mw-content-text" class="mw-body-content"><div class="mw-content-ltr mw-parser-output" lang="es" dir="ltr"><div class="noprint AP rellink"><span style="font-size:88%">Artículo principal:</span>&#32;<i><a href="/wiki/Liga_de_Campeones_de_la_UEFA_2022-23" title="Liga de Campeones de la UEFA 2022-23"> Liga de Campeones de la UEFA 2022-23</a></i></div>
<p>En los <b>Octavos de final de la <a href="/wiki/Liga_de_Campeones_de_la_UEFA_2022-23" title="Liga de Campeones de la UEFA 2022-23">Liga de Campeones de la UEFA 2022-23</a></b>, participaron los dieciséis equipos que terminaron primeros y segundos de cada grupo en la fase anterior. Estos fueron distribuidos en ocho parejas. Cada pareja se enfrentó en partidos de ida y vuelta de 90 minutos cada uno. En estos encuentros no se consideró la <a href="/wiki/Regla_del_gol_de_visitante" title="Regla del gol de visitante">regla del gol de visitante</a>. En caso de que no hubiese ganador en el período regular, se realizaría una prórroga de 30 minutos, y si no hay ganador se realizarían <a href="/wiki/Tiros_desde_el_punto_penal" title="Tiros desde el punto penal">tiros desde el punto penal</a>. El sorteo se realizó el 7 de noviembre de 2022 a las 12:00 en <a href="/wiki/Nyon" title="Nyon">Nyon</a>, <a href="/wiki/Suiza" title="Suiza">Suiza</a>.<sup id="cite_ref-1" class="reference separada"><a href="#cite_note-1"><span class="corchete-llamada">[</span>1<span class="corchete-llamada">]</span></a></sup>&#8203;
</p>
<meta property="mw:PageProp/toc" />
<h2><span id="Cuadro_de_clasificaci.C3.B3n"></span><span class="mw-headline" id="Cuadro_de_clasificación">Cuadro de clasificación</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=1" title="Editar sección: Cuadro de clasificación"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="columns" style="-moz-column-count:2; -webkit-column-count:2; column-count:2;">
</div>
<center>
<table cellspacing="0" style="background: #f9f9f9; border: 1px #aaa solid; border-collapse: collapse;" width="60%">

<tbody><tr style="color:black" bgcolor="#ccddcc">
<th>Grupo
</th>
<th>Bombo 1
<p><span style="white-space:nowrap">(Líderes de grupo)</span>
</p>
</th>
<th>Bombo 2
<p><span style="white-space:nowrap">(Segundos de grupo)</span> 
</p>
</th></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2022-23">A</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2022-23">B</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Belgium_(civil).svg" class="mw-file-description" title="Bandera de Bélgica"><img alt="Bandera de Bélgica" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/20px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/30px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/40px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Club_Brujas" title="Club Brujas">Brujas</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2022-23">C</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2022-23">D</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Eintracht_Fr%C3%A1ncfort" title="Eintracht Fráncfort">Eintracht Fráncfort</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2022-23">E</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2022-23">F</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2022-23">G</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</td></tr>
<tr>
<td align="center"><a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2022-23">H</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a></td>
<td align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a>
</td></tr></tbody></table>
</center>
<h2><span class="mw-headline" id="Participantes">Participantes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=2" title="Editar sección: Participantes"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table width="100%">

<tbody><tr align="center">
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/60px-Flag_of_Portugal.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/120px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/60px-Flag_of_Spain.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/60px-Flag_of_Portugal.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/120px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a>
</th>
<th><a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</th>
<th><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</th>
<th><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</th>
<th><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</th>
<th><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</th>
<th><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</th>
<th><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</th></tr>
<tr>
<th>Clasificado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>Clasificado
</th>
<th>Clasificado
</th></tr>
<tr>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_sscnapoli2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f1/Kit_left_arm_sscnapoli2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_sscnapoli2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/11/Kit_body_sscnapoli2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_sscnapoli2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2f/Kit_right_arm_sscnapoli2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_sscnapoli2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/5f/Kit_socks_sscnapoli2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>	
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5c/Kit_left_arm_fcporto2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d1/Kit_body_fcporto2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_right_arm_fcporto2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e2/Kit_shorts_fcporto2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcporto2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/1/1b/Kit_socks_fcporto2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a7/Kit_left_arm_bayern2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/65/Kit_body_bayern2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_right_arm_bayern2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c7/Kit_shorts_bayern2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bayern2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/30/Kit_socks_bayern2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_left_arm_tottenham2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_body_tottenham2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_right_arm_tottenham2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_tottenham2223H2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/05/Kit_shorts_tottenham2223H2.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7d/Kit_socks_tottenham2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/33/Kit_left_arm_chelsea2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_body_chelsea2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_right_arm_chelsea2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_shorts_chelsea2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/69/Kit_socks_chelsea2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/82/Kit_left_arm_realmadridcf2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_realmadridcf2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_right_arm_realmadridcf2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_shorts_realmadridcf2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadridcf2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b3/Kit_socks_realmadridcf2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_left_arm_mancity2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/49/Kit_body_mancity2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6a/Kit_right_arm_mancity2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/15/Kit_shorts_mancity2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/f6/Kit_socks_mancity2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_benfica2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_body_benfica2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_right_arm_benfica2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th></tr>
<tr align="center">
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th></tr></tbody></table>
<table width="100%">

<tbody><tr align="center">
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/60px-Flag_of_England.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/120px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Belgium_(civil).svg" class="mw-file-description" title="Bandera de Bélgica"><img alt="Bandera de Bélgica" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/60px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/90px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/120px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/60px-Flag_of_Italy.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/60px-Flag_of_Germany.svg.png" decoding="async" width="60" height="36" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/120px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</th>
<th width="12,5%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/60px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="60" height="40" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/90px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/120px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</th></tr>
<tr align="center">
<th><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</th>
<th><a href="/wiki/Club_Brujas" title="Club Brujas">Brujas</a>
</th>
<th><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</th>
<th><a href="/wiki/Eintracht_Fr%C3%A1ncfort" title="Eintracht Fráncfort">Eintracht Fráncfort</a>
</th>
<th><a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a>
</th>
<th><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</th>
<th><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</th>
<th><a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a>
</th></tr>
<tr>
<th>Eliminado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th>
<th>Clasificado
</th>
<th>Eliminado
</th>
<th>Eliminado
</th>
<th>Eliminado
</th></tr>
<tr>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_left_arm_liverpool2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ac/Kit_body_liverpool2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b1/Kit_right_arm_liverpool2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#E00000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#E00000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ad/Kit_left_arm_brugge2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c8/Kit_body_brugge2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e2/Kit_right_arm_brugge2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c1/Kit_shorts_brugge2223H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_brugge2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_socks_brugge2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bb/Kit_left_arm_inter2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_body_inter2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b6/Kit_right_arm_inter2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#fffiff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_shorts_inter2223H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_inter2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/2/29/Kit_socks_inter2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_frankfurt2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d0/Kit_body_frankfurt2223e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b0/Kit_left_arm_milan2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9b/Kit_body_milan2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_right_arm_milan2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_shorts_milan2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_milan2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_milan2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_rbl2223c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e8/Kit_left_arm_rbl2223c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rbl2223C.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/da/Kit_body_rbl2223C.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_rbl2223c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f9/Kit_right_arm_rbl2223c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_rbl2223c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_shorts_rbl2223c.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_left_arm_bvb2223e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_bvb2223e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8d/Kit_right_arm_bvb2223e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bvb2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_shorts_bvb2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/c0/Kit_socks_bvb2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th>
<th>
<div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_left_arm_psg2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/24/Kit_body_psg2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/66/Kit_right_arm_psg2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cd/Kit_shorts_psg2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0A1254"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</th></tr>
<tr align="center">
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th></tr></tbody></table>
<h2><span class="mw-headline" id="Estadios">Estadios</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=3" title="Editar sección: Estadios"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span typeof="mw:File"><a href="/wiki/Archivo:Stadio_Maradona_Serie_A.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/71/Stadio_Maradona_Serie_A.jpg/200px-Stadio_Maradona_Serie_A.jpg" decoding="async" width="200" height="97" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/71/Stadio_Maradona_Serie_A.jpg/300px-Stadio_Maradona_Serie_A.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/71/Stadio_Maradona_Serie_A.jpg/400px-Stadio_Maradona_Serie_A.jpg 2x" data-file-width="3561" data-file-height="1730" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/4/40/Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg/200px-Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/40/Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg/300px-Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/40/Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg/400px-Porto_Est%C3%A1dio_do_Drag%C3%A3o_1.jpg 2x" data-file-width="1300" data-file-height="866" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:M%C3%BCnchen_-_Allianz-Arena_(Luftbild).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/200px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/300px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg/400px-M%C3%BCnchen_-_Allianz-Arena_%28Luftbild%29.jpg 2x" data-file-width="1484" data-file-height="840" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:London_Tottenham_Hotspur_Stadium.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/London_Tottenham_Hotspur_Stadium.jpg/200px-London_Tottenham_Hotspur_Stadium.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/London_Tottenham_Hotspur_Stadium.jpg/300px-London_Tottenham_Hotspur_Stadium.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/London_Tottenham_Hotspur_Stadium.jpg/400px-London_Tottenham_Hotspur_Stadium.jpg 2x" data-file-width="3906" data-file-height="2925" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Estadio_Diego_Armando_Maradona_(Italia)" title="Estadio Diego Armando Maradona (Italia)">Estadio Diego Armando Maradona</a></b>
<p>Ciudad: <a href="/wiki/N%C3%A1poles" title="Nápoles">Nápoles</a><br />
Capacidad: <b>55 000</b> espectadores<br />
Club:  <a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_do_Drag%C3%A3o" class="mw-redirect" title="Estadio do Dragão">Estadio do Dragão</a></b><br />
<p>Ciudad:  <a href="/wiki/Oporto" title="Oporto">Oporto</a><br />
Capacidad: <b>50 033</b> espectadores<br />
Club:  <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</p>
</td>
<td><b><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a></b><br />
<p>Ciudad:  <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a><br />
Capacidad: <b>75 000</b> espectadores<br />
Club:  <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</p>
</td>
<td><b><a href="/wiki/Tottenham_Hotspur_Stadium" title="Tottenham Hotspur Stadium">Tottenham Hotspur Stadium</a></b><br />
<p>Ciudad:  <a href="/wiki/Londres" title="Londres">Londres</a><br />
Capacidad: <b>62 062</b> espectadores<br />
Club:  <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span typeof="mw:File"><a href="/wiki/Archivo:Chelsea_Football_Club,_Stamford_Bridge_11.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg/200px-Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg/300px-Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg/400px-Chelsea_Football_Club%2C_Stamford_Bridge_11.jpg 2x" data-file-width="4608" data-file-height="3456" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Estudio_Lamela_SantiagoBernabeu.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Estudio_Lamela_SantiagoBernabeu.jpg/200px-Estudio_Lamela_SantiagoBernabeu.jpg" decoding="async" width="200" height="157" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Estudio_Lamela_SantiagoBernabeu.jpg/300px-Estudio_Lamela_SantiagoBernabeu.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Estudio_Lamela_SantiagoBernabeu.jpg/400px-Estudio_Lamela_SantiagoBernabeu.jpg 2x" data-file-width="800" data-file-height="627" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Etihad_Stadium_at_night_-_2015.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/200px-Etihad_Stadium_at_night_-_2015.jpg" decoding="async" width="200" height="105" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/300px-Etihad_Stadium_at_night_-_2015.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Etihad_Stadium_at_night_-_2015.jpg/400px-Etihad_Stadium_at_night_-_2015.jpg 2x" data-file-width="1024" data-file-height="537" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Estadio_da_Luz_-_panoramio_(7).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Estadio_da_Luz_-_panoramio_%287%29.jpg/200px-Estadio_da_Luz_-_panoramio_%287%29.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Estadio_da_Luz_-_panoramio_%287%29.jpg/300px-Estadio_da_Luz_-_panoramio_%287%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/11/Estadio_da_Luz_-_panoramio_%287%29.jpg/400px-Estadio_da_Luz_-_panoramio_%287%29.jpg 2x" data-file-width="3600" data-file-height="2397" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Stamford_Bridge_(estadio)" title="Stamford Bridge (estadio)">Stamford Bridge</a></b><br />
<p>Ciudad:  <a href="/wiki/Londres" title="Londres">Londres</a><br />
Capacidad: <b>41 841</b> espectadores<br />
Club:  <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a></b><br />
<p>Ciudad: <a href="/wiki/Madrid" title="Madrid">Madrid</a><br />
Capacidad: <b>81 044</b> espectadores<br />
Club:  <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a></b><br />
<p>Ciudad: <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a><br />
Capacidad: <b>55 097</b> espectadores<br />
Club:  <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</p>
</td>
<td><b><a href="/wiki/Est%C3%A1dio_da_Luz" title="Estádio da Luz">Estádio da Luz</a></b><br />
<p>Ciudad: <a href="/wiki/Lisboa" title="Lisboa">Lisboa</a><br />
Capacidad: <b>66 500</b> espectadores<br />
Club: <a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Panorama_of_Anfield_with_new_main_stand_(29676137824).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/200px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg" decoding="async" width="200" height="136" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/300px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/02/Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg/400px-Panorama_of_Anfield_with_new_main_stand_%2829676137824%29.jpg 2x" data-file-width="3148" data-file-height="2143" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_(2).jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_%282%29.jpg/200px-Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_%282%29.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_%282%29.jpg/300px-Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_%282%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_%282%29.jpg/400px-Panoramio_-_V%26A_Dudush_-_Jan_Breydel_Stadion_%282%29.jpg 2x" data-file-width="1080" data-file-height="719" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Stadio_Meazza.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Stadio_Meazza.jpg/200px-Stadio_Meazza.jpg" decoding="async" width="200" height="124" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/11/Stadio_Meazza.jpg/300px-Stadio_Meazza.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/11/Stadio_Meazza.jpg/400px-Stadio_Meazza.jpg 2x" data-file-width="3608" data-file-height="2232" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Frankfurt_stadium.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Frankfurt_stadium.jpg/200px-Frankfurt_stadium.jpg" decoding="async" width="200" height="120" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Frankfurt_stadium.jpg/300px-Frankfurt_stadium.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Frankfurt_stadium.jpg/400px-Frankfurt_stadium.jpg 2x" data-file-width="2694" data-file-height="1620" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Anfield" title="Anfield">Anfield</a></b><br />
<p>Ciudad:  <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a><br />
Capacidad: <b>54 074</b> espectadores<br />
Club:  <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Jan_Breydel" title="Estadio Jan Breydel">Estadio Jan Breydel</a></b><br />
<p>Ciudad:  <a href="/wiki/Brujas" title="Brujas">Brujas</a><br />
Capacidad: <b>30 000</b> espectadores<br />
Club: <a href="/wiki/Club_Brujas" title="Club Brujas">Brujas</a>
</p>
</td>
<td><b><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">Giuseppe Meazza/San Siro</a></b> <br />
<p>Ciudad:  <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a> <br />
Capacidad: <b>80 018</b> espectadores<br />
Club:  <a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a> y <a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a>
</p>
</td>
<td><b><a href="/wiki/Deutsche_Bank_Park" title="Deutsche Bank Park">Deutsche Bank Park</a></b> <br />
<p>Ciudad:  <a href="/wiki/Fr%C3%A1ncfort" class="mw-redirect" title="Fráncfort">Fráncfort</a> <br />
Capacidad: <b>48 500</b> espectadores<br />
Club:  <a href="/wiki/Eintracht_Fr%C3%A1ncfort" title="Eintracht Fráncfort">Eintracht Fráncfort</a>
</p>
</td></tr></tbody></table>
<table border="0" cellspacing="1" cellpadding="0" style="font-size: 90%;" width="85%" align="center">
<tbody><tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td></tr>
<tr align="center">
<td><span typeof="mw:File"><a href="/wiki/Archivo:Leipzig_stadium.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Leipzig_stadium.jpg/200px-Leipzig_stadium.jpg" decoding="async" width="200" height="150" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Leipzig_stadium.jpg/300px-Leipzig_stadium.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Leipzig_stadium.jpg/400px-Leipzig_stadium.jpg 2x" data-file-width="4775" data-file-height="3576" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:Signal_iduna_park_stadium_dortmund_2.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Signal_iduna_park_stadium_dortmund_2.jpg/200px-Signal_iduna_park_stadium_dortmund_2.jpg" decoding="async" width="200" height="133" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Signal_iduna_park_stadium_dortmund_2.jpg/300px-Signal_iduna_park_stadium_dortmund_2.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Signal_iduna_park_stadium_dortmund_2.jpg/400px-Signal_iduna_park_stadium_dortmund_2.jpg 2x" data-file-width="4470" data-file-height="2980" /></a></span>
</td>
<td><span typeof="mw:File"><a href="/wiki/Archivo:PSG-Lyon_Parc_des_Princes_02.jpg" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ef/PSG-Lyon_Parc_des_Princes_02.jpg/200px-PSG-Lyon_Parc_des_Princes_02.jpg" decoding="async" width="200" height="113" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ef/PSG-Lyon_Parc_des_Princes_02.jpg/300px-PSG-Lyon_Parc_des_Princes_02.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ef/PSG-Lyon_Parc_des_Princes_02.jpg/400px-PSG-Lyon_Parc_des_Princes_02.jpg 2x" data-file-width="3724" data-file-height="2096" /></a></span>
</td></tr>
<tr align="center" valign="top" bgcolor="87CEEB" style="border:1px solid #aaa;">
<td><b><a href="/wiki/Red_Bull_Arena_(Leipzig)" title="Red Bull Arena (Leipzig)">Red Bull Arena</a></b><br />
<p>Ciudad:  <a href="/wiki/Leipzig" title="Leipzig">Leipzig</a><br />
Capacidad: <b>47 069</b> espectadores<br />
Club:  <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</p>
</td>
<td><b><a href="/wiki/Signal_Iduna_Park" title="Signal Iduna Park">Signal Iduna Park</a></b><br />
<p>Ciudad: <a href="/wiki/Dortmund" title="Dortmund">Dortmund</a><br />
Capacidad: <b>81 365</b> espectadores<br />
Club:  <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</p>
</td>
<td><b><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a></b><br />
<p>Ciudad: <a href="/wiki/Par%C3%ADs" title="París">París</a><br />
Capacidad: <b>47 929</b> espectadores<br />
Club:  <a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">Paris Saint-Germain</a>
</p>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Llaves">Llaves</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=4" title="Editar sección: Llaves"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table class="wikitable" style="text-align:center">



<tbody><tr>
<th style="text-align:right; width:250px">Equipo 1
</th>
<th style="width:80px"><abbr title="Resultado global">Agr.</abbr>
</th>
<th style="text-align:left; width:250px">Equipo 2
</th>
<th style="width:80px">Ida
</th>
<th style="width:80px">Vuelta
</th></tr>
<tr>
<td style="text-align: right;"><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">1–8
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#RBL_MCI">1–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MCI_RBL">0–7</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Club_Brujas" title="Club Brujas">Brujas</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Belgium_(civil).svg" class="mw-file-description" title="Bandera de Bélgica"><img alt="Bandera de Bélgica" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/20px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/30px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/40px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">1–7
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <b><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BRU_BEN">0–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BEN_BRU">1–5</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="text-align: center;">2–6
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <b><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#LIV_RMA">2–5</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#RMA_LIV">0–1</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a></b> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="text-align: center;">1–0
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#MIL_TOT">1–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#TOT_MIL">0–0</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Eintracht_Fr%C3%A1ncfort" title="Eintracht Fráncfort">Eintracht Fráncfort</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">0–5
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <b><a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#EIN_NAP">0–2</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#NAP_EIN">0–3</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">1–2
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <b><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#DOR_CHE">1–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#CHE_DOR">0–2</a>
</td></tr>

<tr>
<td style="text-align: right;background-color: #CCFFCC;"><b><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span></b>
</td>
<td style="text-align: center;">1–0
</td>
<td style="text-align: left;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#INT_POR">1–0</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#POR_INT">0–0</a>
</td></tr>

<tr>
<td style="text-align: right;"><a href="/wiki/Paris_Saint-Germain_Football_Club" title="Paris Saint-Germain Football Club">París Saint-Germain</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td style="text-align: center;">0–3
</td>
<td style="text-align: left;background-color: #CCFFCC;"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <b><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></b>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#PSG_BAY">0–1</a>
</td>
<td style="text-align: center;"><a class="mw-selflink-fragment" href="#BAY_PSG">0–2</a>
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Enfrentamientos">Enfrentamientos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=5" title="Editar sección: Enfrentamientos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li>Los horarios de los partidos corresponden a la <a href="/wiki/Hora_central_europea" title="Hora central europea">hora central europea</a> (CET <a href="/wiki/UTC%2B01:00" title="UTC+01:00">UTC+1</a>).</li></ul>
<h3><span id="Leipzig_.E2.80.93_Manchester_City"></span><span class="mw-headline" id="Leipzig_–_Manchester_City">Leipzig – Manchester City</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=6" title="Editar sección: Leipzig – Manchester City"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="RBL_MCI">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 22 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:1 <style data-mw-deduplicate="TemplateStyles:r144106874">.mw-parser-output .sinnegrita,.mw-parser-output .sinnegrita b{font-weight:normal}</style><span class="sinnegrita">(0:1)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Red_Bull_Arena_(Leipzig)" title="Red Bull Arena (Leipzig)">Red Bull Arena</a>,</span> <a href="/wiki/Leipzig" title="Leipzig">Leipzig</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right"><a href="/wiki/Jo%C5%A1ko_Gvardiol" title="Joško Gvardiol">Gvardiol</a> <span typeof="mw:File"><span title="Anotado en el minuto 70"><img alt="Anotado en el minuto 70" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">70'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036588--leipzig-vs-man-city/">Reporte</a>
</td>
<td valign="top" align="left"><a href="/wiki/Riyad_Mahrez" title="Riyad Mahrez">Mahrez</a> <span typeof="mw:File"><span title="Anotado en el minuto 27"><img alt="Anotado en el minuto 27" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">27'</small>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 45&#160;228 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Serdar_G%C3%B6z%C3%BCb%C3%BCy%C3%BCk&amp;action=edit&amp;redlink=1" class="new" title="Serdar Gözübüyük (aún no redactado)">Serdar Gözübüyük</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Pol_van_Boekel" title="Pol van Boekel">Pol van Boekel</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_rbl2223c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e8/Kit_left_arm_rbl2223c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rbl2223C.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/da/Kit_body_rbl2223C.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_rbl2223c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f9/Kit_right_arm_rbl2223c.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_rbl2223c.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_shorts_rbl2223c.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2223a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/35/Kit_left_arm_mancity2223a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2223a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_body_mancity2223a.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2223a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/24/Kit_right_arm_mancity2223a.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_mancity2223a.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/53/Kit_shorts_mancity2223a.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2223a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_socks_mancity2223a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MCI_LEI">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 14 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>7:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(3:0)</span></b> </div><div style="font-size: 85%">(Global <b>8:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/RasenBallsport_Leipzig" title="RasenBallsport Leipzig">Leipzig</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Ciudad_de_M%C3%A1nchester" title="Estadio Ciudad de Mánchester">Etihad Stadium</a>,</span> <a href="/wiki/M%C3%A1nchester" title="Mánchester">Mánchester</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Erling_Haaland" title="Erling Haaland">Haaland</a> <span typeof="mw:File"><span title="Anotado en los minutos 22, 24, 45+2, 53&#160;y 57"><img alt="Anotado en los minutos 22, 24, 45+2, 53&#160;y 57" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">22'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small>,&#160;<small style="vertical-align: middle;">24'</small>,&#160;<small style="vertical-align: middle;">45+2'</small>,&#160;<small style="vertical-align: middle;">53'</small>,&#160;<small style="vertical-align: middle;">57'</small></li>
<li><a href="/wiki/%C4%B0lkay_G%C3%BCndo%C4%9Fan" title="İlkay Gündoğan">Gündoğan</a> <span typeof="mw:File"><span title="Anotado en el minuto 49"><img alt="Anotado en el minuto 49" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">49'</small></li>
<li><a href="/wiki/Kevin_De_Bruyne" title="Kevin De Bruyne">De Bruyne</a> <span typeof="mw:File"><span title="Anotado en el minuto 90+2"><img alt="Anotado en el minuto 90+2" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">90+2'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036594--man-city-vs-leipzig/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 52&#160;038 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Slovenia.svg" class="mw-file-description" title="Bandera de Eslovenia"><img alt="Bandera de Eslovenia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/20px-Flag_of_Slovenia.svg.png" decoding="async" width="20" height="10" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/30px-Flag_of_Slovenia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/40px-Flag_of_Slovenia.svg.png 2x" data-file-width="1200" data-file-height="600" /></a></span></span> <a href="/wiki/Slavko_Vin%C4%8Di%C4%87" title="Slavko Vinčić">Slavko Vinčić</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_left_arm_mancity2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/49/Kit_body_mancity2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6a/Kit_right_arm_mancity2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_mancity2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/15/Kit_shorts_mancity2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_mancity2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/f6/Kit_socks_mancity2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_rbl2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/52/Kit_body_rbl2223T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Brujas_.E2.80.93_Benfica"></span><span class="mw-headline" id="Brujas_–_Benfica">Brujas – Benfica</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=7" title="Editar sección: Brujas – Benfica"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BRU_BEN">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 15 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Club_Brujas" title="Club Brujas">Brujas</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Belgium_(civil).svg" class="mw-file-description" title="Bandera de Bélgica"><img alt="Bandera de Bélgica" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/20px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/30px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/40px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:2 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Jan_Breydel" title="Estadio Jan Breydel">Estadio Jan Breydel</a>,</span> <a href="/wiki/Brujas" title="Brujas">Brujas</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036584--club-brugge-vs-benfica/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><a href="/wiki/Jo%C3%A3o_M%C3%A1rio_(futbolista_nacido_en_1993)" title="João Mário (futbolista nacido en 1993)">João Mário</a> <span typeof="mw:File"><span title="Anotado en el minuto 51"><img alt="Anotado en el minuto 51" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">51'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small></li>
<li><a href="/wiki/David_Neres" title="David Neres">Neres</a> <span typeof="mw:File"><span title="Anotado en el minuto 88"><img alt="Anotado en el minuto 88" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">88'</small></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 24&#160;136 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Davide_Massa" title="Davide Massa">Davide Massa</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/w/index.php?title=Paolo_Valeri&amp;action=edit&amp;redlink=1" class="new" title="Paolo Valeri (aún no redactado)">Paolo Valeri</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ad/Kit_left_arm_brugge2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c8/Kit_body_brugge2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e2/Kit_right_arm_brugge2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_brugge2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c1/Kit_shorts_brugge2223H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_brugge2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/f/fd/Kit_socks_brugge2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_benfica2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_body_benfica2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_right_arm_benfica2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BEN_BRU">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 7 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>5:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(2:0)</span></b> </div><div style="font-size: 85%">(Global <b>7:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Belgium_(civil).svg" class="mw-file-description" title="Bandera de Bélgica"><img alt="Bandera de Bélgica" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/20px-Flag_of_Belgium_%28civil%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/30px-Flag_of_Belgium_%28civil%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Belgium_%28civil%29.svg/40px-Flag_of_Belgium_%28civil%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Club_Brujas" title="Club Brujas">Brujas</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Est%C3%A1dio_da_Luz" title="Estádio da Luz">Estádio da Luz</a>,</span> <a href="/wiki/Lisboa" title="Lisboa">Lisboa</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Rafa_Silva" title="Rafa Silva">Rafa Silva</a> <span typeof="mw:File"><span title="Anotado en el minuto 38"><img alt="Anotado en el minuto 38" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">38'</small></li>
<li><a href="/wiki/Gon%C3%A7alo_Ramos" title="Gonçalo Ramos">Ramos</a> <span typeof="mw:File"><span title="Anotado en los minutos 45+2&#160;y 57"><img alt="Anotado en los minutos 45+2&#160;y 57" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">45+2'</small>,&#160;<small style="vertical-align: middle;">57'</small></li>
<li><a href="/wiki/Jo%C3%A3o_M%C3%A1rio_(futbolista_nacido_en_1993)" title="João Mário (futbolista nacido en 1993)">João Mário</a> <span typeof="mw:File"><span title="Anotado en el minuto 71"><img alt="Anotado en el minuto 71" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">71'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small></li>
<li><a href="/wiki/David_Neres" title="David Neres">Neres</a> <span typeof="mw:File"><span title="Anotado en el minuto 77"><img alt="Anotado en el minuto 77" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">77'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036590--benfica-vs-club-brugge/">Reporte</a>
</td>
<td valign="top" align="left"><a href="/wiki/Bjorn_Meijer" title="Bjorn Meijer">Meijer</a> <span typeof="mw:File"><span title="Anotado en el minuto 87"><img alt="Anotado en el minuto 87" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">87'</small>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 60&#160;960 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Turkey.svg" class="mw-file-description" title="Bandera de Turquía"><img alt="Bandera de Turquía" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/20px-Flag_of_Turkey.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/30px-Flag_of_Turkey.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/40px-Flag_of_Turkey.svg.png 2x" data-file-width="1200" data-file-height="800" /></a></span></span> <a href="/w/index.php?title=Halil_Umut_Meler&amp;action=edit&amp;redlink=1" class="new" title="Halil Umut Meler (aún no redactado)">Halil Umut Meler</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Juan_Mart%C3%ADnez_Munuera" title="Juan Martínez Munuera">Martínez Munuera</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_left_arm_benfica2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/46/Kit_body_benfica2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_benfica2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_right_arm_benfica2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_adidasred.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/48/Kit_shorts_adidasred.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_3_stripes_white.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_3_stripes_white.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0f1012"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_brugge2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e0/Kit_left_arm_brugge2223T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0f1012"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_brugge2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9c/Kit_body_brugge2223T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0f1012"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_brugge2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e2/Kit_right_arm_brugge2223T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0f1012"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_brugge2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1e/Kit_shorts_brugge2223T.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0f1012"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Liverpool_.E2.80.93_Real_Madrid"></span><span class="mw-headline" id="Liverpool_–_Real_Madrid">Liverpool – Real Madrid</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=8" title="Editar sección: Liverpool – Real Madrid"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="LIV_RMA">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 21 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:5 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(2:2)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Anfield" title="Anfield">Anfield</a>,</span> <a href="/wiki/Liverpool" title="Liverpool">Liverpool</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Darwin_N%C3%BA%C3%B1ez" title="Darwin Núñez">Núñez</a> <span typeof="mw:File"><span title="Anotado en el minuto 4"><img alt="Anotado en el minuto 4" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">4'</small></li>
<li><a href="/wiki/Mohamed_Salah" title="Mohamed Salah">Salah</a> <span typeof="mw:File"><span title="Anotado en el minuto 14"><img alt="Anotado en el minuto 14" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">14'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036586--liverpool-vs-real-madrid/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><a href="/wiki/Vin%C3%ADcius_J%C3%BAnior" title="Vinícius Júnior">Vinícius Júnior</a> <span typeof="mw:File"><span title="Anotado en los minutos 21&#160;y 36"><img alt="Anotado en los minutos 21&#160;y 36" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">21'</small>,&#160;<small style="vertical-align: middle;">36'</small></li>
<li><a href="/wiki/%C3%89der_Milit%C3%A3o" title="Éder Militão">Éder Militão</a> <span typeof="mw:File"><span title="Anotado en el minuto 47"><img alt="Anotado en el minuto 47" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">47'</small></li>
<li><a href="/wiki/Karim_Benzema" title="Karim Benzema">Benzema</a> <span typeof="mw:File"><span title="Anotado en los minutos 55&#160;y 67"><img alt="Anotado en los minutos 55&#160;y 67" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">55'</small>,&#160;<small style="vertical-align: middle;">67'</small></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 52&#160;337 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Romania.svg" class="mw-file-description" title="Bandera de Rumania"><img alt="Bandera de Rumania" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/20px-Flag_of_Romania.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/30px-Flag_of_Romania.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/40px-Flag_of_Romania.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Istv%C3%A1n_Kov%C3%A1cs" title="István Kovács">István Kovács</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_left_arm_liverpool2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ac/Kit_body_liverpool2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b1/Kit_right_arm_liverpool2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#E00000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#E00000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/82/Kit_left_arm_realmadridcf2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_realmadridcf2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_right_arm_realmadridcf2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_shorts_realmadridcf2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadridcf2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b3/Kit_socks_realmadridcf2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="RMA_LIV">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 15 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div><div style="font-size: 85%">(Global <b>6:2</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Liverpool_Football_Club" title="Liverpool Football Club">Liverpool</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Santiago_Bernab%C3%A9u" title="Estadio Santiago Bernabéu">Estadio Santiago Bernabéu</a>,</span> <a href="/wiki/Madrid" title="Madrid">Madrid</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Karim_Benzema" title="Karim Benzema">Benzema</a> <span typeof="mw:File"><span title="Anotado en el minuto 78"><img alt="Anotado en el minuto 78" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">78'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036596--real-madrid-vs-liverpool/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 63&#160;127 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Felix_Zwayer" title="Felix Zwayer">Felix Zwayer</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Marco_Fritz&amp;action=edit&amp;redlink=1" class="new" title="Marco Fritz (aún no redactado)">Marco Fritz</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/82/Kit_left_arm_realmadridcf2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_realmadridcf2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/45/Kit_right_arm_realmadridcf2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_realmadridcf2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d2/Kit_shorts_realmadridcf2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_realmadridcf2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/b/b3/Kit_socks_realmadridcf2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_left_arm_liverpool2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ac/Kit_body_liverpool2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_liverpool2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b1/Kit_right_arm_liverpool2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#E00000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#E00000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Milan_.E2.80.93_Tottenham_Hotspur"></span><span class="mw-headline" id="Milan_–_Tottenham_Hotspur">Milan – Tottenham Hotspur</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=9" title="Editar sección: Milan – Tottenham Hotspur"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="MIL_TOT">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 14 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:0)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">San Siro</a>,</span> <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right"><a href="/wiki/Brahim_D%C3%ADaz" title="Brahim Díaz">Díaz</a> <span typeof="mw:File"><span title="Anotado en el minuto 7"><img alt="Anotado en el minuto 7" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">7'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036582--milan-vs-tottenham/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 74&#160;320 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Switzerland.svg" class="mw-file-description" title="Bandera de Suiza"><img alt="Bandera de Suiza" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/20px-Flag_of_Switzerland.svg.png" decoding="async" width="20" height="20" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/30px-Flag_of_Switzerland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/40px-Flag_of_Switzerland.svg.png 2x" data-file-width="512" data-file-height="512" /></a></span></span> <a href="/w/index.php?title=Sandro_Sch%C3%A4rer&amp;action=edit&amp;redlink=1" class="new" title="Sandro Schärer (aún no redactado)">Sandro Schärer</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/w/index.php?title=Marco_Fritz&amp;action=edit&amp;redlink=1" class="new" title="Marco Fritz (aún no redactado)">Marco Fritz</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#7D0B1D"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b0/Kit_left_arm_milan2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#7D0B1D"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9b/Kit_body_milan2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#7D0B1D"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_right_arm_milan2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_shorts_milan2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_milan2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_milan2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_left_arm_tottenham2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_body_tottenham2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_right_arm_tottenham2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_tottenham2223H2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/05/Kit_shorts_tottenham2223H2.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7d/Kit_socks_tottenham2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="TOT_MIL">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 8 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Tottenham_Hotspur_Football_Club" title="Tottenham Hotspur Football Club">Tottenham Hotspur</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:0</b> </div><div style="font-size: 85%">(Global <b>0:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Tottenham_Hotspur_Stadium" title="Tottenham Hotspur Stadium">Tottenham Hotspur Stadium</a>,</span> <a href="/wiki/Londres" title="Londres">Londres</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036592--tottenham-vs-milan/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 61&#160;602 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Cl%C3%A9ment_Turpin" title="Clément Turpin">Clément Turpin</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/3f/Kit_left_arm_tottenham2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_body_tottenham2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_tottenham2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/64/Kit_right_arm_tottenham2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_tottenham2223H2.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/05/Kit_shorts_tottenham2223H2.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_tottenham2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7d/Kit_socks_tottenham2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#7D0B1D"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b0/Kit_left_arm_milan2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#7D0B1D"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9b/Kit_body_milan2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#7D0B1D"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f7/Kit_right_arm_milan2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_milan2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1a/Kit_shorts_milan2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_milan2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/e/ef/Kit_socks_milan2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Eintracht_Fr.C3.A1ncfort_.E2.80.93_Napoli"></span><span class="mw-headline" id="Eintracht_Fráncfort_–_Napoli">Eintracht Fráncfort – Napoli</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=10" title="Editar sección: Eintracht Fráncfort – Napoli"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="EIN_NAP">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 21 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Eintracht_Fr%C3%A1ncfort" title="Eintracht Fráncfort">Eintracht Fráncfort</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:2 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:1)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Deutsche_Bank_Park" title="Deutsche Bank Park">Deutsche Bank Park</a>,</span> <a href="/wiki/Fr%C3%A1ncfort" class="mw-redirect" title="Fráncfort">Fráncfort</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036587--frankfurt-vs-napoli/">Reporte</a>
</td>
<td valign="top" align="left">
<ul><li><a href="/wiki/Victor_Osimhen" title="Victor Osimhen">Osimhen</a> <span typeof="mw:File"><span title="Anotado en el minuto 40"><img alt="Anotado en el minuto 40" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">40'</small></li>
<li><a href="/wiki/Giovanni_Di_Lorenzo" title="Giovanni Di Lorenzo">Di Lorenzo</a> <span typeof="mw:File"><span title="Anotado en el minuto 65"><img alt="Anotado en el minuto 65" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">65'</small></li></ul>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 47&#160;500 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/Artur_Dias" class="mw-redirect" title="Artur Dias">Artur Dias</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/w/index.php?title=Tiago_Martins&amp;action=edit&amp;redlink=1" class="new" title="Tiago Martins (aún no redactado)">Tiago Martins</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_frankfurt2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d0/Kit_body_frankfurt2223e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#000000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#000000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_sscnapoli2223ae.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/42/Kit_left_arm_sscnapoli2223ae.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_sscnapoli2223ae.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/68/Kit_body_sscnapoli2223ae.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_sscnapoli2223ae.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/24/Kit_right_arm_sscnapoli2223ae.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_sscnapoli2122a.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_socks_sscnapoli2122a.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="NAP_EIN">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 15 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>3:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:0)</span></b> </div><div style="font-size: 85%">(Global <b>5:0</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Eintracht_Fr%C3%A1ncfort" title="Eintracht Fráncfort">Eintracht Fráncfort</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Diego_Armando_Maradona_(Italia)" title="Estadio Diego Armando Maradona (Italia)">Estadio Diego Armando Maradona</a>,</span> <a href="/wiki/N%C3%A1poles" title="Nápoles">Nápoles</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Victor_Osimhen" title="Victor Osimhen">Osimhen</a> <span typeof="mw:File"><span title="Anotado en los minutos 45+2&#160;y 53"><img alt="Anotado en los minutos 45+2&#160;y 53" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">45+2'</small>,&#160;<small style="vertical-align: middle;">53'</small></li>
<li><a href="/wiki/Piotr_Zieli%C5%84ski" title="Piotr Zieliński">Zieliński</a> <span typeof="mw:File"><span title="Anotado en el minuto 64"><img alt="Anotado en el minuto 64" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">64'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036597--napoli-vs-frankfurt/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Anthony_Taylor_(%C3%A1rbitro)" title="Anthony Taylor (árbitro)">Anthony Taylor</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Pol_van_Boekel" title="Pol van Boekel">Pol van Boekel</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_sscnapoli2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f1/Kit_left_arm_sscnapoli2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_sscnapoli2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/11/Kit_body_sscnapoli2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_sscnapoli2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2f/Kit_right_arm_sscnapoli2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_sscnapoli2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/5/5f/Kit_socks_sscnapoli2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_left.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/67/Kit_left_arm_left.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_frankfurt2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b7/Kit_body_frankfurt2223T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_right.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/16/Kit_right_arm_right.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_shorts.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/19/Kit_shorts_shorts.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Borussia_Dortmund_.E2.80.93_Chelsea"></span><span class="mw-headline" id="Borussia_Dortmund_–_Chelsea">Borussia Dortmund – Chelsea</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=11" title="Editar sección: Borussia Dortmund – Chelsea"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="DOR_CHE">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 15 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Signal_Iduna_Park" title="Signal Iduna Park">Signal Iduna Park</a>,</span> <a href="/wiki/Dortmund" title="Dortmund">Dortmund</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right"><a href="/wiki/Karim_Adeyemi" title="Karim Adeyemi">Adeyemi</a> <span typeof="mw:File"><span title="Anotado en el minuto 63"><img alt="Anotado en el minuto 63" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">63'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036585--dortmund-vs-chelsea/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 81&#160;365 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Jes%C3%BAs_Gil_Manzano" title="Jesús Gil Manzano">Gil Manzano</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/20px-Flag_of_Spain.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/30px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/40px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span> <a href="/wiki/Alejandro_Jos%C3%A9_Hern%C3%A1ndez_Hern%C3%A1ndez" title="Alejandro José Hernández Hernández">Hernández Hernández</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_left_arm_bvb2223e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_bvb2223e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8d/Kit_right_arm_bvb2223e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bvb2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_shorts_bvb2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/c0/Kit_socks_bvb2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/33/Kit_left_arm_chelsea2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_body_chelsea2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_right_arm_chelsea2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_shorts_chelsea2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/69/Kit_socks_chelsea2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="CHE_DOR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 7 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(1:0)</span></b> </div><div style="font-size: 85%">(Global <b>2:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Borussia_Dortmund" title="Borussia Dortmund">Borussia Dortmund</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Stamford_Bridge_(estadio)" title="Stamford Bridge (estadio)">Stamford Bridge</a>,</span> <a href="/wiki/Londres" title="Londres">Londres</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Raheem_Sterling" title="Raheem Sterling">Sterling</a> <span typeof="mw:File"><span title="Anotado en el minuto 43"><img alt="Anotado en el minuto 43" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">43'</small></li>
<li><a href="/wiki/Kai_Havertz" title="Kai Havertz">Havertz</a> <span typeof="mw:File"><span title="Anotado en el minuto 53"><img alt="Anotado en el minuto 53" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">53'&#160;(<a href="/wiki/Tiro_penal_(f%C3%BAtbol)" class="mw-redirect" title="Tiro penal (fútbol)">pen.</a>)</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036591--chelsea-vs-dortmund/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 38&#160;882 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Danny_Makkelie" title="Danny Makkelie">Danny Makkelie</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_the_Netherlands.svg" class="mw-file-description" title="Bandera de los Países Bajos"><img alt="Bandera de los Países Bajos" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/20px-Flag_of_the_Netherlands.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/30px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/40px-Flag_of_the_Netherlands.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Pol_van_Boekel" title="Pol van Boekel">Pol van Boekel</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/33/Kit_left_arm_chelsea2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_body_chelsea2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/4/4c/Kit_right_arm_chelsea2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_chelsea2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/09/Kit_shorts_chelsea2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_chelsea2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/6/69/Kit_socks_chelsea2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/88/Kit_left_arm_bvb2223e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/eb/Kit_body_bvb2223e.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bvb2223e.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/8d/Kit_right_arm_bvb2223e.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bvb2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ab/Kit_shorts_bvb2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bvb2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/c/c0/Kit_socks_bvb2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Inter_de_Mil.C3.A1n_.E2.80.93_Porto"></span><span class="mw-headline" id="Inter_de_Milán_–_Porto">Inter de Milán – Porto</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=12" title="Editar sección: Inter de Milán – Porto"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="INT_POR">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 22 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>1:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span> <a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_Giuseppe_Meazza" title="Estadio Giuseppe Meazza">Giuseppe Meazza</a>,</span> <a href="/wiki/Mil%C3%A1n" title="Milán">Milán</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right"><a href="/wiki/Romelu_Lukaku" title="Romelu Lukaku">Lukaku</a> <span typeof="mw:File"><span title="Anotado en el minuto 86"><img alt="Anotado en el minuto 86" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">86'</small>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036589--inter-vs-porto/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 75&#160;374 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Serbia.svg" class="mw-file-description" title="Bandera de Serbia"><img alt="Bandera de Serbia" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/20px-Flag_of_Serbia.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/30px-Flag_of_Serbia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/40px-Flag_of_Serbia.svg.png 2x" data-file-width="1350" data-file-height="900" /></a></span></span> <a href="/wiki/Sr%C4%91an_Jovanovi%C4%87" title="Srđan Jovanović">Srđan Jovanović</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bastian_Dankert" title="Bastian Dankert">Bastian Dankert</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bb/Kit_left_arm_inter2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/bc/Kit_body_inter2223H.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b6/Kit_right_arm_inter2223H.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#fffiff"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_inter2223H.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_shorts_inter2223H.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_inter2223H.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/2/29/Kit_socks_inter2223H.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFF081"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcporto2223t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/1/1e/Kit_left_arm_fcporto2223t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFF081"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcporto2223t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/6e/Kit_body_fcporto2223t.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFF081"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcporto2223t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/ae/Kit_right_arm_fcporto2223t.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#DCDDE1"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_fcporto2223t.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/b/b4/Kit_shorts_fcporto2223t.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#DCDDE1"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcporto2223t.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/73/Kit_socks_fcporto2223t.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="POR_INT">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 14 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/F%C3%BAtbol_Club_Oporto" title="Fútbol Club Oporto">Porto</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/20px-Flag_of_Portugal.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/30px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/40px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:0</b> </div><div style="font-size: 85%">(Global <b>0:1</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Estadio_do_Drag%C3%A3o" class="mw-redirect" title="Estadio do Dragão">Estadio do Dragão</a>,</span> <a href="/wiki/Oporto" title="Oporto">Oporto</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036595--porto-vs-inter/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 48&#160;015 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/wiki/Szymon_Marciniak" title="Szymon Marciniak">Szymon Marciniak</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/w/index.php?title=Tomasz_Kwiatkowski&amp;action=edit&amp;redlink=1" class="new" title="Tomasz Kwiatkowski (aún no redactado)">Tomasz Kwiatkowski</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/5c/Kit_left_arm_fcporto2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d1/Kit_body_fcporto2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/f/f5/Kit_right_arm_fcporto2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_fcporto2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/e/e2/Kit_shorts_fcporto2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_fcporto2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/1/1b/Kit_socks_fcporto2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_inter2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/0/0e/Kit_left_arm_inter2223T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_inter2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/62/Kit_body_inter2223T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_inter2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/3/37/Kit_right_arm_inter2223T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_inter2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/85/Kit_shorts_inter2223T.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_inter2223T.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_socks_inter2223T.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h3><span id="Par.C3.ADs_Saint-Germain_.E2.80.93_Bayern_M.C3.BAnich"></span><span class="mw-headline" id="París_Saint-Germain_–_Bayern_Múnich">París Saint-Germain – Bayern Múnich</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=13" title="Editar sección: París Saint-Germain – Bayern Múnich"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h3>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="PSG_BAY">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Ida; 14 de febrero de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>0:1 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span> <a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Parque_de_los_Pr%C3%ADncipes" title="Parque de los Príncipes">Parque de los Príncipes</a>,</span> <a href="/wiki/Par%C3%ADs" title="París">París</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036583--paris-vs-bayern/">Reporte</a>
</td>
<td valign="top" align="left"><a href="/wiki/Kingsley_Coman" title="Kingsley Coman">Coman</a> <span typeof="mw:File"><span title="Anotado en el minuto 53"><img alt="Anotado en el minuto 53" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">53'</small>
</td>
<td colspan="2" valign="top" align="left">Asistencia: 46&#160;435 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/20px-Flag_of_England.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/30px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span> <a href="/wiki/Michael_Oliver_(%C3%A1rbitro)" title="Michael Oliver (árbitro)">Michael Oliver</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Poland.svg" class="mw-file-description" title="Bandera de Polonia"><img alt="Bandera de Polonia" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/20px-Flag_of_Poland.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/30px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/40px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400" /></a></span></span> <a href="/w/index.php?title=Tomasz_Kwiatkowski&amp;action=edit&amp;redlink=1" class="new" title="Tomasz Kwiatkowski (aún no redactado)">Tomasz Kwiatkowski</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/2e/Kit_left_arm_psg2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/2/24/Kit_body_psg2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/66/Kit_right_arm_psg2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#0A1254"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_psg2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/cd/Kit_shorts_psg2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#0A1254"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a7/Kit_left_arm_bayern2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/65/Kit_body_bayern2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_right_arm_bayern2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c7/Kit_shorts_bayern2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bayern2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/30/Kit_socks_bayern2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<div style="width: 100%; background-color: transparent; clear:both" class="vevent" id="BAY_PSG">
</div> 
<table cellspacing="0" class="collapsible autocollapse vevent plainlist" width="100%" style="height:20px; border-top:1px solid #999999; border-bottom:1px solid #999999; background:#;padding-left:.23em;">

<tbody><tr>
<td style="width:20%;vertical-align:top;text-align:left;font-size:82%">Vuelta; 8 de marzo de 2023
</td>
<td width="24%" valign="top" align="right"><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a> <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/20px-Flag_of_Germany.svg.png" decoding="async" width="20" height="12" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/30px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/40px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td>
<td width="12%" valign="top" align="center">
<div style="white-space:nowrap;"><b>2:0 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r144106874"><span class="sinnegrita">(0:0)</span></b> </div><div style="font-size: 85%">(Global <b>3:0</b>)</div>
</td>
<td width="22%" valign="top" align="left"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_France_(1794%E2%80%931815,_1830%E2%80%931974).svg" class="mw-file-description" title="Bandera de Francia"><img alt="Bandera de Francia" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/20px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/30px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg/40px-Flag_of_France_%281794%E2%80%931815%2C_1830%E2%80%931974%29.svg.png 2x" data-file-width="900" data-file-height="600" /></a></span></span> <a href="/wiki/Par%C3%ADs_Saint-Germain_Football_Club" class="mw-redirect" title="París Saint-Germain Football Club">París Saint-Germain</a>
</td>
<td style="vertical-align:top;text-align:left;font-size:82%;"><span style="white-space:nowrap"><a href="/wiki/Allianz_Arena" title="Allianz Arena">Allianz Arena</a>,</span> <a href="/wiki/M%C3%BAnich" title="Múnich">Múnich</a>
</td>
<th width="2%" style="vertical-align:top;font-size: 85%" rowspan="2">
</th></tr>

<tr style="font-size:85%">
<td style="vertical-align:top;text-align:left;font-size:100%;">21:00
</td>
<td valign="top" align="right">
<ul><li><a href="/wiki/Eric_Maxim_Choupo-Moting" title="Eric Maxim Choupo-Moting">Choupo-Moting</a> <span typeof="mw:File"><span title="Anotado en el minuto 61"><img alt="Anotado en el minuto 61" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">61'</small></li>
<li><a href="/wiki/Serge_Gnabry" title="Serge Gnabry">Gnabry</a> <span typeof="mw:File"><span title="Anotado en el minuto 90"><img alt="Anotado en el minuto 90" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/13px-Soccerball_shade.svg.png" decoding="async" width="13" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/20px-Soccerball_shade.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/51/Soccerball_shade.svg/26px-Soccerball_shade.svg.png 2x" data-file-width="333" data-file-height="333" /></span></span>&#160;<small style="vertical-align: middle;">90'</small></li></ul>
</td>
<td valign="top" align="center"><a rel="nofollow" class="external text" href="https://es.uefa.com/uefachampionsleague/match/2036593--bayern-vs-paris/">Reporte</a>
</td>
<td valign="top" align="left">
</td>
<td colspan="2" valign="top" align="left">Asistencia: 75&#160;000 espectadores<br />Árbitro: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Daniele_Orsato" title="Daniele Orsato">Daniele Orsato</a><br />VAR: <span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/20px-Flag_of_Italy.svg.png" decoding="async" width="20" height="13" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/30px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/40px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span> <a href="/wiki/Massimiliano_Irrati" title="Massimiliano Irrati">Massimiliano Irrati</a>
</td></tr>

</tbody></table>
<table class="wikitable collapsible collapsed" style="text-align: center; margin: 0 auto; width: 100%; background:White;">
<tbody><tr>
<th colspan="2">Uniformes
</th></tr>
<tr>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/a/a7/Kit_left_arm_bayern2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/6/65/Kit_body_bayern2223h.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/d/d4/Kit_right_arm_bayern2223h.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FF0000"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_bayern2223h.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/c/c7/Kit_shorts_bayern2223h.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FF0000"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_bayern2223h.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/3/30/Kit_socks_bayern2223h.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td>
<td><div style="width: 100px; margin: 0 auto; padding: 0;">
<div style="position: relative; left: 0px; top: 0px; width: 100px; height: 120px; margin: 0 auto; padding: 0;">
<div style="position: absolute; left: 0px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_left_arm_psg2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/7/73/Kit_left_arm_psg2223T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 31px; top: 0px; width: 38px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_body_psg2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/8/86/Kit_body_psg2223T.png" decoding="async" width="38" height="59" class="mw-file-element" data-file-width="38" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 69px; top: 0px; width: 31px; height: 59px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_right_arm_psg2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/5/55/Kit_right_arm_psg2223T.png" decoding="async" width="31" height="59" class="mw-file-element" data-file-width="31" data-file-height="59" /></a></span></div>
<div style="position: absolute; left: 0px; top: 59px; width: 100px; height: 36px; background-color:#FFFFFF"><span class="mw-default-size" typeof="mw:File"><a href="/wiki/Archivo:Kit_shorts_psg2223T.png" class="mw-file-description"><img src="//upload.wikimedia.org/wikipedia/commons/9/9c/Kit_shorts_psg2223T.png" decoding="async" width="100" height="36" class="mw-file-element" data-file-width="100" data-file-height="36" /></a></span></div>
<div style="position: absolute; left: 0px; top: 95px; width: 100px; height: 25px; background-color:#FFFFFF"><span class="mw-default-size mw-valign-top" typeof="mw:File"><a href="/wiki/Archivo:Kit_socks_socks.png" class="mw-file-description"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/7/7c/Kit_socks_socks.png" decoding="async" width="100" height="25" class="mw-file-element" data-file-width="100" data-file-height="25" /></a></span></div>
</div>
</div>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Clasificados_para_Cuartos_de_final">Clasificados para Cuartos de final</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=14" title="Editar sección: Clasificados para Cuartos de final"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<table align="center" cellpadding="2" cellspacing="0" style="background: #f5faff; border: 1px #aaa solid; border-collapse: collapse; font-size: 95%;" width="80%">

<tbody><tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Portugal.svg" class="mw-file-description" title="Bandera de Portugal"><img alt="Bandera de Portugal" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/45px-Flag_of_Portugal.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/68px-Flag_of_Portugal.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/90px-Flag_of_Portugal.svg.png 2x" data-file-width="600" data-file-height="400" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Spain.svg" class="mw-file-description" title="Bandera de España"><img alt="Bandera de España" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/45px-Flag_of_Spain.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/68px-Flag_of_Spain.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/90px-Flag_of_Spain.svg.png 2x" data-file-width="750" data-file-height="500" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/45px-Flag_of_Italy.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/68px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Manchester_City_Football_Club" title="Manchester City Football Club">Manchester City</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Sport_Lisboa_e_Benfica" title="Sport Lisboa e Benfica">Benfica</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Real_Madrid_Club_de_F%C3%BAtbol" title="Real Madrid Club de Fútbol">Real Madrid</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Associazione_Calcio_Milan" title="Associazione Calcio Milan">Milan</a></b>
</td></tr>
<tr align="center">
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/45px-Flag_of_Italy.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/68px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_England.svg" class="mw-file-description" title="Bandera de Inglaterra"><img alt="Bandera de Inglaterra" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/45px-Flag_of_England.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/68px-Flag_of_England.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/90px-Flag_of_England.svg.png 2x" data-file-width="800" data-file-height="480" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Italy.svg" class="mw-file-description" title="Bandera de Italia"><img alt="Bandera de Italia" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/45px-Flag_of_Italy.svg.png" decoding="async" width="45" height="30" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/68px-Flag_of_Italy.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/90px-Flag_of_Italy.svg.png 2x" data-file-width="1500" data-file-height="1000" /></a></span></span>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/wiki/Archivo:Flag_of_Germany.svg" class="mw-file-description" title="Bandera de Alemania"><img alt="Bandera de Alemania" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/45px-Flag_of_Germany.svg.png" decoding="async" width="45" height="27" class="mw-file-element" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/68px-Flag_of_Germany.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/90px-Flag_of_Germany.svg.png 2x" data-file-width="1000" data-file-height="600" /></a></span></span>
</td></tr>
<tr align="center" style="border-bottom:1px solid #aaa;">
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Societ%C3%A0_Sportiva_Calcio_Napoli" title="Società Sportiva Calcio Napoli">Napoli</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Chelsea_Football_Club" title="Chelsea Football Club">Chelsea</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Inter_de_Mil%C3%A1n" title="Inter de Milán">Inter de Milán</a></b>
</td>
<td style="border-right:1px solid #aaa;" width="25%"><b><a href="/wiki/Bayern_de_M%C3%BAnich" title="Bayern de Múnich">Bayern Múnich</a></b>
</td></tr></tbody></table>
<h2><span id="V.C3.A9ase_tambi.C3.A9n"></span><span class="mw-headline" id="Véase_también">Véase también</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=15" title="Editar sección: Véase también"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/Anexo:Ronda_preliminar_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Ronda preliminar de la Liga de Campeones de la UEFA 2022-23">Anexo: Ronda preliminar de la Liga de Campeones de la UEFA 2022-23</a></li>
<li><a href="/wiki/Anexo:Primera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Primera ronda previa de la Liga de Campeones de la UEFA 2022-23">Anexo: Primera ronda previa de la Liga de Campeones de la UEFA 2022-23</a></li>
<li><a href="/wiki/Anexo:Segunda_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Segunda ronda previa de la Liga de Campeones de la UEFA 2022-23">Anexo: Segunda ronda previa de la Liga de Campeones de la UEFA 2022-23</a></li>
<li><a href="/wiki/Anexo:Tercera_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Tercera ronda previa de la Liga de Campeones de la UEFA 2022-23">Anexo: Tercera ronda previa de la Liga de Campeones de la UEFA 2022-23</a></li>
<li><a href="/wiki/Anexo:Cuarta_ronda_previa_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Cuarta ronda previa de la Liga de Campeones de la UEFA 2022-23">Anexo:Cuarta ronda previa de la Liga de Campeones de la UEFA 2022-23</a></li>
<li>Fase de grupos <small>(<a href="/wiki/Anexo:Grupo_A_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo A de la Liga de Campeones de la UEFA 2022-23">Grupo A</a>, <a href="/wiki/Anexo:Grupo_B_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo B de la Liga de Campeones de la UEFA 2022-23">Grupo B</a>, <a href="/wiki/Anexo:Grupo_C_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo C de la Liga de Campeones de la UEFA 2022-23">Grupo C</a>, <a href="/wiki/Anexo:Grupo_D_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo D de la Liga de Campeones de la UEFA 2022-23">Grupo D</a>, <a href="/wiki/Anexo:Grupo_E_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo E de la Liga de Campeones de la UEFA 2022-23">Grupo E</a>, <a href="/wiki/Anexo:Grupo_F_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo F de la Liga de Campeones de la UEFA 2022-23">Grupo F</a>, <a href="/wiki/Anexo:Grupo_G_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo G de la Liga de Campeones de la UEFA 2022-23">Grupo G</a>, <a href="/wiki/Anexo:Grupo_H_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Grupo H de la Liga de Campeones de la UEFA 2022-23">Grupo H</a>)</small></li>
<li><a href="/wiki/Anexo:Cuartos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Cuartos de final de la Liga de Campeones de la UEFA 2022-23">Anexo: Cuartos de final de la Liga de Campeones de la UEFA 2022-23</a></li>
<li><a href="/wiki/Anexo:Semifinales_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Anexo:Semifinales de la Liga de Campeones de la UEFA 2022-23">Anexo: Semifinales de la Liga de Campeones de la UEFA 2022-23</a></li>
<li><a href="/wiki/Final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23" title="Final de la Liga de Campeones de la UEFA 2022-23">Final de la Liga de Campeones de la UEFA 2022-23</a></li></ul>
<h2><span class="mw-headline" id="Referencias">Referencias</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=16" title="Editar sección: Referencias"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="listaref" style="list-style-type: decimal;"><ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><a href="#cite_ref-1">↑</a></span> <span class="reference-text"><span class="citation web"><a rel="nofollow" class="external text" href="https://www.marca.com/futbol/champions-league/2022/11/02/635f9936268e3ed2168b4591.html">«Sorteo octavos de Champions League: cuándo es, equipos clasificados y bombos»</a>. <i>MARCA</i>. 2 de noviembre de 2022<span class="reference-accessdate">. Consultado el 2 de noviembre de 2022</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fes.wikipedia.org%3AAnexo%3AOctavos+de+final+de+la+Liga+de+Campeones+de+la+UEFA+2022-23&amp;rft.atitle=Sorteo+octavos+de+Champions+League%3A+cu%C3%A1ndo+es%2C+equipos+clasificados+y+bombos&amp;rft.date=2022-11-02&amp;rft.genre=article&amp;rft.jtitle=MARCA&amp;rft_id=https%3A%2F%2Fwww.marca.com%2Ffutbol%2Fchampions-league%2F2022%2F11%2F02%2F635f9936268e3ed2168b4591.html&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
</ol></div>
<h2><span class="mw-headline" id="Enlaces_externos">Enlaces externos</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;action=edit&amp;section=17" title="Editar sección: Enlaces externos"><span>editar</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://es.uefa.com">Página oficial de la UEFA</a></li>
<li><a rel="nofollow" class="external text" href="http://es.uefa.com/uefachampionsleague/index.html">Página oficial de la UEFA Champions League</a></li></ul>
<p><br clear="all" />
</p>
<table class="wikitable" border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; margin:0 auto;">

<tbody><tr style="text-align: center;">
<td width="30%">Predecesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2021-22" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2021-22">2021-22</a></b>
</td>
<td width="40%"><b>Octavos de final de la<br /><a href="/wiki/Liga_de_Campeones_de_la_UEFA" title="Liga de Campeones de la UEFA">Liga de Campeones de la UEFA</a></b><br />2022-23
</td>
<td width="30%">Sucesor:<br /><b><a href="/wiki/Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2023-24" title="Anexo:Octavos de final de la Liga de Campeones de la UEFA 2023-24">2023-24</a></b>
</td></tr></tbody></table>
<!-- 
NewPP limit report
Parsed by mw‐api‐int.codfw.main‐774c7d5bcb‐z9hlc
Cached time: 20240212175348
Cache expiry: 2592000
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.664 seconds
Real time usage: 0.846 seconds
Preprocessor visited node count: 23990/1000000
Post‐expand include size: 235460/2097152 bytes
Template argument size: 78805/2097152 bytes
Highest expansion depth: 14/100
Expensive parser function count: 0/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 3934/5000000 bytes
Lua time usage: 0.058/10.000 seconds
Lua memory usage: 1875404/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  407.415      1 -total
 60.62%  246.975     16 Plantilla:Partidos
 19.94%   81.250     80 Plantilla:Bandera
 16.08%   65.517     64 Plantilla:En_varias_líneas
 10.02%   40.827     32 Plantilla:Árbitro
  8.70%   35.456     16 Plantilla:Str_sub
  8.09%   32.957     32 Plantilla:Trim
  7.68%   31.278    120 Plantilla:Bandera_icono
  6.65%   27.103      1 Plantilla:Listaref
  6.06%   24.678     23 Plantilla:Camisetas
-->

<!-- Saved in parser cache with key eswiki:pcache:idhash:10376179-0!canonical and timestamp 20240212175347 and revision id 157852274. Rendering was triggered because: api-parse
 -->
</div><!--esi <esi:include src="/esitest-fa8a495983347898/content" /> --><noscript><img src="https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" width="1" height="1" style="border: none; position: absolute;"></noscript>
<div class="printfooter" data-nosnippet="">Obtenido de «<a dir="ltr" href="https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;oldid=157852274">https://es.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;oldid=157852274</a>»</div></div>
					<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Especial:Categor%C3%ADas" title="Especial:Categorías">Categoría</a>: <ul><li><a href="/wiki/Categor%C3%ADa:Liga_de_Campeones_de_la_UEFA_2022-23" title="Categoría:Liga de Campeones de la UEFA 2022-23">Liga de Campeones de la UEFA 2022-23</a></li></ul></div></div>
				</div>
			</main>
			
		</div>
		<div class="mw-footer-container">
			
<footer id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info">
	<li id="footer-info-lastmod"> Esta página se editó por última vez el 29 ene 2024 a las 23:39.</li>
	<li id="footer-info-copyright">El texto está disponible bajo la <a rel="license" href="https://es.wikipedia.org/wiki/Wikipedia:Texto_de_la_Licencia_Creative_Commons_Atribuci%C3%B3n-CompartirIgual_4.0_Internacional">Licencia Creative Commons Atribución-CompartirIgual 4.0</a><a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es" style="display:none;"></a>; pueden aplicarse cláusulas adicionales. Al usar este sitio aceptas nuestros <a href="https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/es">términos de uso</a> y nuestra <a href="https://foundation.wikimedia.org/wiki/Policy:Privacy_policy/es">política de privacidad</a>.<br/>Wikipedia&reg; es una marca registrada de la <a href="https://wikimediafoundation.org/es/">Fundación Wikimedia</a>, una organización sin ánimo de lucro.</li>
</ul>

	<ul id="footer-places">
	<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy/es">Política de privacidad</a></li>
	<li id="footer-places-about"><a href="/wiki/Wikipedia:Acerca_de">Acerca de Wikipedia</a></li>
	<li id="footer-places-disclaimers"><a href="/wiki/Wikipedia:Limitaci%C3%B3n_general_de_responsabilidad">Limitación de responsabilidad</a></li>
	<li id="footer-places-wm-codeofconduct"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct">Código de conducta</a></li>
	<li id="footer-places-developers"><a href="https://developer.wikimedia.org">Desarrolladores</a></li>
	<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/es.wikipedia.org">Estadísticas</a></li>
	<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement/es">Declaración de cookies</a></li>
	<li id="footer-places-mobileview"><a href="//es.m.wikipedia.org/w/index.php?title=Anexo:Octavos_de_final_de_la_Liga_de_Campeones_de_la_UEFA_2022-23&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Versión para móviles</a></li>
</ul>

	<ul id="footer-icons" class="noprint">
	<li id="footer-copyrightico"><a href="https://wikimediafoundation.org/"><img src="/static/images/footer/wikimedia-button.png" srcset="/static/images/footer/wikimedia-button-1.5x.png 1.5x, /static/images/footer/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation" loading="lazy" /></a></li>
	<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img src="/static/images/footer/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/footer/poweredby_mediawiki_132x47.png 1.5x, /static/images/footer/poweredby_mediawiki_176x62.png 2x" width="88" height="31" loading="lazy"></a></li>
</ul>

</footer>

		</div>
	</div> 
</div> 
<div class="vector-settings" id="p-dock-bottom">
	<ul>
		<li>
		<button class="cdx-button cdx-button--icon-only vector-limited-width-toggle" id=""><span class="vector-icon mw-ui-icon-fullScreen mw-ui-icon-wikimedia-fullScreen"></span>

<span>Activar o desactivar el límite de anchura del contenido</span>
</button>
</li>
	</ul>
</div>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgHostname":"mw1354","wgBackendResponseTime":113,"wgPageParseReport":{"limitreport":{"cputime":"0.664","walltime":"0.846","ppvisitednodes":{"value":23990,"limit":1000000},"postexpandincludesize":{"value":235460,"limit":2097152},"templateargumentsize":{"value":78805,"limit":2097152},"expansiondepth":{"value":14,"limit":100},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":3934,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  407.415      1 -total"," 60.62%  246.975     16 Plantilla:Partidos"," 19.94%   81.250     80 Plantilla:Bandera"," 16.08%   65.517     64 Plantilla:En_varias_líneas"," 10.02%   40.827     32 Plantilla:Árbitro","  8.70%   35.456     16 Plantilla:Str_sub","  8.09%   32.957     32 Plantilla:Trim","  7.68%   31.278    120 Plantilla:Bandera_icono","  6.65%   27.103      1 Plantilla:Listaref","  6.06%   24.678     23 Plantilla:Camisetas"]},"scribunto":{"limitreport-timeusage":{"value":"0.058","limit":"10.000"},"limitreport-memusage":{"value":1875404,"limit":52428800}},"cachereport":{"origin":"mw-api-int.codfw.main-774c7d5bcb-z9hlc","timestamp":"20240212175348","ttl":2592000,"transientcontent":false}}});});</script>
</body>
</html>"""

#Crear un objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
tabla = soup.find('table', {'class': 'wikitable', 'style': 'text-align:center'})

#Verificamos si esta
if tabla:
    #Obtener todas las filas y celdas de la tabla
	rows = tabla.find_all('tr')

	#Crear una lista para almacenas las filas de datos
	tabla_data = []

	#Recorrer cada fila y extraer el texto de las celdas
	for row in rows:
		cells = row.find_all(['td', 'th'])
		row_data = [cell.get_text(strip=True) for cell in cells]
		tabla_data.append(row_data)

	print(tabulate(tabla_data, headers="firstrow", tablefmt="pretty"))

else:
	print('No se encontró la tabla')